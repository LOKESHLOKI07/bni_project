# Generated by Django 5.1.3 on 2024-12-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='bulleted_list',
            field=models.JSONField(default=list),
        ),
    ]