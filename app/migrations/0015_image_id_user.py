# Generated by Django 4.1.5 on 2023-01-27 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]