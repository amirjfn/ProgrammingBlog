# Generated by Django 4.2 on 2023-05-07 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_my_file_article_slug_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 1, 24, 34, 478505, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
