# Generated by Django 4.2.7 on 2024-01-16 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0004_remove_usermy_image_alter_usermy_profil_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermy',
            old_name='profil_image',
            new_name='profile_image',
        ),
    ]
