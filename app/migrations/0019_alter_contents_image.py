# Generated by Django 4.1.5 on 2023-01-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_contents_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
