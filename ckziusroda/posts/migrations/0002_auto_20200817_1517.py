# Generated by Django 3.1 on 2020-08-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('category', 'slug')},
        ),
    ]