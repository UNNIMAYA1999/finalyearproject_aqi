# Generated by Django 2.1.2 on 2018-11-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerify_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerifyapi',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='aerifyapi',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
