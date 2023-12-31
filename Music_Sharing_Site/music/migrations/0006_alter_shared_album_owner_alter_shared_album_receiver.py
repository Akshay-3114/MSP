# Generated by Django 4.1.2 on 2023-06-16 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_auto_20200417_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shared_album',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_album_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shared_album',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_album_receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
