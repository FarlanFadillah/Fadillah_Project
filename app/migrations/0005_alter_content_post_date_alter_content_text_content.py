# Generated by Django 4.1.5 on 2023-01-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_content_id_user_content_like_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='post_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='text_content',
            field=models.TextField(max_length=300, null=True),
        ),
    ]