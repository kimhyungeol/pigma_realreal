# Generated by Django 4.1.2 on 2022-10-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MTV', '0005_alter_board_image_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='file_upload',
        ),
        migrations.RemoveField(
            model_name='board',
            name='image_upload',
        ),
        migrations.AddField(
            model_name='board',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo'),
        ),
        migrations.AddField(
            model_name='board',
            name='sound',
            field=models.FileField(blank=True, null=True, upload_to='blog_sound'),
        ),
    ]
