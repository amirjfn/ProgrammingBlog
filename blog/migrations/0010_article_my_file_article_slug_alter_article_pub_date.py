# Generated by Django 4.2 on 2023-05-07 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_article_is_published_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='my_file',
            field=models.FileField(null=True, upload_to='file'),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 1, 7, 12, 572886, tzinfo=datetime.timezone.utc)),
        ),
    ]
