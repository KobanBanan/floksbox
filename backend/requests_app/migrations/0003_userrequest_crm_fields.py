from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests_app', '0002_product_image_unfold'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='manager_notes',
            field=models.TextField(blank=True, default='', verbose_name='Заметки менеджера'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='source',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Источник'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='status',
            field=models.CharField(
                choices=[
                    ('new', 'Новая'),
                    ('in_progress', 'В работе'),
                    ('completed', 'Завершена'),
                    ('cancelled', 'Отменена'),
                ],
                default='new',
                max_length=20,
                verbose_name='Статус',
            ),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Телефон'),
        ),
    ]
