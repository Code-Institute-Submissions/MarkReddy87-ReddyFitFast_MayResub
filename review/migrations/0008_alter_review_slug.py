# Generated by Django 3.2 on 2022-04-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_alter_review_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]