# Generated by Django 2.2.7 on 2019-11-21 08:10

import Blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('image', models.ImageField(upload_to=Blog.models.generate_filename, verbose_name='Изображение')),
                ('body', models.TextField(verbose_name='Содержание')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Лайки')),
                ('dislikes', models.PositiveIntegerField(default=0, verbose_name='Дизлайки')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]