# Generated by Django 4.2.7 on 2024-01-17 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0026_kurs_commen_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kurs',
            old_name='commen_num',
            new_name='comment_num',
        ),
    ]