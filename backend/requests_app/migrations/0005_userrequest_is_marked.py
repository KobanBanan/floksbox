from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requests_app", "0004_product_image_optional"),
    ]

    operations = [
        migrations.AddField(
            model_name="userrequest",
            name="is_marked",
            field=models.BooleanField(default=False, verbose_name="Помечено"),
        ),
    ]
