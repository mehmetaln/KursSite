# Generated by Django 4.2.7 on 2024-01-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0028_kurs_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurs',
            name='date_now',
            field=models.DateTimeField(default='-', verbose_name='Tarih - Saat'),
        ),
    ]