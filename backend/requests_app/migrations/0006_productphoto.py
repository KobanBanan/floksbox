from django.core.validators import FileExtensionValidator
from django.db import migrations, models
import django.db.models.deletion
import requests_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("requests_app", "0005_userrequest_is_marked"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductPhoto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=requests_app.models.product_gallery_path,
                        validators=[
                            requests_app.models.validate_image_size,
                            FileExtensionValidator(["jpg", "jpeg", "png", "webp"]),
                        ],
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "position",
                    models.PositiveIntegerField(default=0, verbose_name="Порядок"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="requests_app.product",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото товара",
                "verbose_name_plural": "Фото товара",
                "ordering": ["position", "id"],
            },
        ),
    ]
