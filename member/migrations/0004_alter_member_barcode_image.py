# Generated by Django 4.2.4 on 2023-08-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_member_barcode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='barcode_image',
            field=models.ImageField(blank=True, default=1, upload_to='barcode_images/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
