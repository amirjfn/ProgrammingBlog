# Generated by Django 4.2 on 2023-05-04 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_alter_article_pub_date_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 4, 20, 0, 35, 752692, tzinfo=datetime.timezone.utc)),
        ),
    ]
