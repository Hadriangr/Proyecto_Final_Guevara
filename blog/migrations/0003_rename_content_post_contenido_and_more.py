# Generated by Django 5.0 on 2023-12-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_tittle_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]