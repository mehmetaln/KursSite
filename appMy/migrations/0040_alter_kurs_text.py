# Generated by Django 4.2.7 on 2024-01-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0039_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='text',
            field=models.TextField(default=0, max_length=5000, verbose_name='Acıklama'),
        ),
    ]