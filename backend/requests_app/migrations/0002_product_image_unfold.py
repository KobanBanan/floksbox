from django.core.validators import FileExtensionValidator
from django.db import migrations, models
import requests_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("requests_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image_unfold",
            field=models.ImageField(
                blank=True,
                help_text="Схема развертки коробки (опционально)",
                null=True,
                upload_to=requests_app.models.product_unfold_image_path,
                validators=[
                    requests_app.models.validate_image_size,
                    FileExtensionValidator(["jpg", "jpeg", "png", "webp"]),
                ],
                verbose_name="Развертка",
            ),
        ),
    ]
