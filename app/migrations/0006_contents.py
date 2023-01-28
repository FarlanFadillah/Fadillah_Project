# Generated by Django 4.1.5 on 2023-01-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_content_post_date_alter_content_text_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('number_content', models.IntegerField()),
                ('text_content', models.TextField(max_length=300)),
                ('post_date', models.DateTimeField()),
                ('like_count', models.IntegerField()),
            ],
        ),
    ]
