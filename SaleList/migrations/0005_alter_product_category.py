# Generated by Django 4.2.4 on 2023-08-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaleList', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('RK', '쌀(잡곡)/김치'), ('FV', '과일/채소'), ('MES', '정육/달걀/해산물'), ('FS', '냉동식품/과자'), ('ETC', '기타')], max_length=500),
        ),
    ]
