# Generated by Django 4.1.5 on 2023-01-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_content_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='id_user',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='number_content',
            field=models.IntegerField(default=0),
        ),
    ]