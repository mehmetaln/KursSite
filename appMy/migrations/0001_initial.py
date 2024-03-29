# Generated by Django 4.2.7 on 2024-01-02 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlik')),
                ('alt_title', models.CharField(max_length=50, verbose_name='Alt Başlık')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlik')),
                ('img', models.ImageField(upload_to='kurs', verbose_name='Resim')),
                ('puan', models.IntegerField(default=0, verbose_name='Puan')),
                ('price', models.IntegerField(default=0, verbose_name='Fiyat')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
