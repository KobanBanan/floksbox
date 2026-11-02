from django.core.validators import FileExtensionValidator
from django.db import migrations, models
import requests_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("requests_app", "0003_userrequest_crm_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Изображение товара (JPG, PNG, WebP, до 5MB)",
                null=True,
                upload_to=requests_app.models.product_image_path,
                validators=[
                    requests_app.models.validate_image_size,
                    FileExtensionValidator(["jpg", "jpeg", "png", "webp"]),
                ],
                verbose_name="Изображение",
            ),
        ),
    ]
