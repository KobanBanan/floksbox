from django.db import migrations, models


def hide_size_where_unused(apps, schema_editor):
    Product = apps.get_model("requests_app", "Product")
    Product.objects.filter(
        category__name__in=[
            "Четырехклапанные коробки",
            "Офсетная печать",
            "Подарочные пакеты",
            "Гофроупаковка с флексопечатью",
        ]
    ).update(show_size=False)


class Migration(migrations.Migration):

    dependencies = [
        ("requests_app", "0006_productphoto"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="show_size",
            field=models.BooleanField(
                default=True,
                help_text="Размер и объём на странице товара",
                verbose_name="Показывать размер",
            ),
        ),
        migrations.RunPython(hide_size_where_unused, migrations.RunPython.noop),
    ]
