# Generated by Django 3.2 on 2022-04-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_remove_review_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
