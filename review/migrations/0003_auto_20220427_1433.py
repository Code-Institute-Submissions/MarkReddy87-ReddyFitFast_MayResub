# Generated by Django 3.2 on 2022-04-27 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0002_alter_review_posted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='test', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_from', to=settings.AUTH_USER_MODEL),
        ),
    ]
