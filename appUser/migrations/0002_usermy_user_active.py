# Generated by Django 4.2.7 on 2024-01-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermy',
            name='user_active',
            field=models.CharField(default=0, max_length=50, verbose_name='Kullancı Dogrulama Linki'),
        ),
    ]
