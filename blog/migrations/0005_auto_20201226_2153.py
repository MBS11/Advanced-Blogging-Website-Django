# Generated by Django 3.1.4 on 2020-12-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='material',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='static/img'),
        ),
    ]
