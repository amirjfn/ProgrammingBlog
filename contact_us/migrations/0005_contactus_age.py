# Generated by Django 4.2 on 2023-05-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0004_contactus_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]