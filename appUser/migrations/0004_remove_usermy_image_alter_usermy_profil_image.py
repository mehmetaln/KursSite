# Generated by Django 4.2.7 on 2024-01-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_usermy_profil_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermy',
            name='image',
        ),
        migrations.AlterField(
            model_name='usermy',
            name='profil_image',
            field=models.ImageField(max_length=200, upload_to='profile', verbose_name='Profil Resmi'),
        ),
    ]
