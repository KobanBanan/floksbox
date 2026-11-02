import json
import os
from decimal import Decimal, InvalidOperation

from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST

from .models import Category, Product, ProductPhoto, validate_image_size

LOGIN = "/admin/login/"
ALLOWED = FileExtensionValidator(["jpg", "jpeg", "png", "webp"])


def _category_or_first(category_id):
    categories = Category.objects.order_by("name")
    if category_id:
        chosen = categories.filter(pk=category_id).first()
        if chosen:
            return categories, chosen
    return categories, categories.first()


def gallery_slots(product):
    slots = []
    if product.image:
        slots.append({"slot": "cover", "url": product.image.url})
    if product.image_unfold:
        slots.append({"slot": "unfold", "url": product.image_unfold.url})
    for photo in product.photos.all():
        if photo.image:
            slots.append({"slot": str(photo.id), "url": photo.image.url})
    return slots


def _check_upload(upload):
    ALLOWED(upload)
    validate_image_size(upload)


def _next_position(product):
    last = product.photos.order_by("-position", "-id").first()
    return (last.position + 1) if last else 0


def _copy_to_cover(product, fieldfile):
    name = os.path.basename(fieldfile.name)
    data = fieldfile.read()
    fieldfile.close()
    product.image.save(name, ContentFile(data), save=True)


def _promote_cover(product):
    product.refresh_from_db()
    if product.image:
        return
    if product.image_unfold:
        _copy_to_cover(product, product.image_unfold)
        product.image_unfold.delete(save=False)
        product.image_unfold = None
        product.save(update_fields=["image_unfold"])
        return
    photo = product.photos.order_by("position", "id").first()
    if photo is None or not photo.image:
        return
    _copy_to_cover(product, photo.image)
    photo.image.delete(save=False)
    photo.delete()


def _store_image(product, upload):
    if not product.image:
        product.image.save(upload.name, upload, save=True)
        return "cover", product.image.url
    photo = ProductPhoto(product=product, position=_next_position(product))
    photo.image.save(upload.name, upload, save=True)
    return str(photo.id), photo.image.url


@staff_member_required(login_url=LOGIN)
def desk(request):
    categories, category = _category_or_first(request.GET.get("category"))
    products = []
    if category is not None:
        products = Product.objects.filter(category=category).order_by("-created_at", "name")
    return render(
        request,
        "desk/index.html",
        {
            "categories": categories,
            "category": category,
            "products": products,
        },
    )


@staff_member_required(login_url=LOGIN)
@require_POST
def desk_create(request):
    try:
        data = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Некорректные данные"}, status=400)

    category = get_object_or_404(Category, pk=data.get("category"))
    product = Product(
        name="Новый товар",
        description="Новый товар",
        category=category,
        height=10,
        width=10,
        depth=10,
        is_active=False,
        show_size=False,
    )
    try:
        product.full_clean(exclude=["image", "image_unfold"])
        product.save()
    except ValidationError as exc:
        message = "; ".join(
            f"{', '.join(errors)}" for errors in exc.message_dict.values()
        )
        return JsonResponse({"ok": False, "error": message or "Не удалось создать"}, status=400)
    return JsonResponse({"ok": True, "id": product.id, "next": f"/desk/product/{product.id}/"})


def _error_text(exc):
    if getattr(exc, "message_dict", None):
        return "; ".join(", ".join(errors) for errors in exc.message_dict.values())
    return "; ".join(getattr(exc, "messages", []) or ["Проверьте поля"])


def _parse_size(raw):
    text = (raw or "").strip().replace(",", ".")
    if not text:
        raise ValidationError("Укажите размер")
    try:
        return Decimal(text)
    except InvalidOperation as exc:
        raise ValidationError("Размер должен быть числом") from exc


def _save_product(product):
    try:
        product.full_clean(exclude=["image", "image_unfold"])
        product.save()
    except ValidationError as exc:
        return _error_text(exc)
    return ""


@staff_member_required(login_url=LOGIN)
def desk_part(request, product_id, part):
    return redirect(f"/desk/product/{product_id}/")


@staff_member_required(login_url=LOGIN)
@require_http_methods(["GET", "POST"])
def desk_edit(request, product_id):
    product = get_object_or_404(
        Product.objects.select_related("category").prefetch_related("photos"),
        pk=product_id,
    )
    error = ""
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        if not name:
            error = "Нужно название"
        else:
            product.name = name[:200]
            product.description = request.POST.get("description") or ""
            product.show_size = request.POST.get("show_size") == "1"
            product.is_active = request.POST.get("is_active") == "1"
            category = Category.objects.filter(pk=request.POST.get("category")).first()
            if category is None:
                error = "Выберите раздел"
            else:
                product.category = category
            if not error and product.show_size:
                try:
                    product.height = _parse_size(request.POST.get("height"))
                    product.width = _parse_size(request.POST.get("width"))
                    product.depth = _parse_size(request.POST.get("depth"))
                except ValidationError as exc:
                    error = _error_text(exc)
            if not error:
                error = _save_product(product)
        if not error:
            return redirect(f"/desk/product/{product.id}/?saved=1")
    product.desk_photos = gallery_slots(product)
    return render(
        request,
        "desk/edit.html",
        {
            "categories": Category.objects.order_by("name"),
            "category": product.category,
            "product": product,
            "saved": request.GET.get("saved") == "1",
            "error": error,
        },
    )


@staff_member_required(login_url=LOGIN)
@require_POST
def desk_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.image:
        product.image.delete(save=False)
    if product.image_unfold:
        product.image_unfold.delete(save=False)
    for photo in product.photos.all():
        if photo.image:
            photo.image.delete(save=False)
    product.delete()
    return JsonResponse({"ok": True})


@staff_member_required(login_url=LOGIN)
@require_POST
def desk_image(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    uploads = request.FILES.getlist("image")
    if not uploads:
        return JsonResponse({"ok": False, "error": "Файл не пришёл"}, status=400)

    added = []
    for upload in uploads:
        try:
            _check_upload(upload)
        except ValidationError as exc:
            return JsonResponse({"ok": False, "error": "; ".join(exc.messages)}, status=400)
        slot, url = _store_image(product, upload)
        added.append({"slot": slot, "url": url})
    return JsonResponse({"ok": True, "photos": added})


@staff_member_required(login_url=LOGIN)
@require_POST
def desk_image_remove(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        data = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"ok": False, "error": "Некорректные данные"}, status=400)

    slot = str(data.get("slot") or "")
    if slot == "cover":
        if product.image:
            product.image.delete(save=False)
            product.image = None
            product.save(update_fields=["image"])
        _promote_cover(product)
    elif slot == "unfold":
        if product.image_unfold:
            product.image_unfold.delete(save=False)
            product.image_unfold = None
            product.save(update_fields=["image_unfold"])
    elif slot.isdigit():
        photo = product.photos.filter(pk=int(slot)).first()
        if photo is None:
            return JsonResponse({"ok": False, "error": "Фото уже нет"}, status=404)
        if photo.image:
            photo.image.delete(save=False)
        photo.delete()
    else:
        return JsonResponse({"ok": False, "error": "Неизвестное фото"}, status=400)

    product.refresh_from_db()
    return JsonResponse({"ok": True, "photos": gallery_slots(product)})
