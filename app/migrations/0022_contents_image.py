# Generated by Django 4.1.5 on 2023-01-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_contents_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='image',
            field=models.ImageField(default='None', upload_to='images/'),
        ),
    ]