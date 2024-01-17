# Generated by Django 4.2.7 on 2024-01-17 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0038_remove_kurs_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.kurs', verbose_name='Begenilen Kurs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Begenen Kullanci')),
            ],
        ),
    ]
