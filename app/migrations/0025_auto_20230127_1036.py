# Generated by Django 4.1.5 on 2023-01-27 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_contents_image'),
    ]

    operations = [
        migrations.RemoveField(
        model_name ='Contents',
        name ='image',
    ),
    ]
