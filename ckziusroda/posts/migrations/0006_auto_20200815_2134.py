# Generated by Django 3.1 on 2020-08-15 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200815_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='public',
            new_name='Opublikuj',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='Treść',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='Tytuł',
        ),
    ]
