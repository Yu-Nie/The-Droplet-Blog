# Generated by Django 4.2 on 2023-04-26 03:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_websitemeta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitemeta',
            name='description',
        ),
        migrations.RemoveField(
            model_name='websitemeta',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
