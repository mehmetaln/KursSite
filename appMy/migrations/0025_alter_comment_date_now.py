# Generated by Django 4.2.7 on 2024-01-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0024_alter_kurs_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih ve Saat'),
        ),
    ]
