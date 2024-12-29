# Generated by Django 5.1.3 on 2024-12-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0002_company_bulleted_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='bulleted_list',
        ),
        migrations.AddField(
            model_name='company',
            name='bullet_points',
            field=models.TextField(blank=True, help_text='Each new line starts with a bullet (*).', null=True),
        ),
    ]