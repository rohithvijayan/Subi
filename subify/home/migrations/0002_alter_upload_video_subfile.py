# Generated by Django 5.0.6 on 2024-06-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_video',
            name='subfile',
            field=models.FileField(upload_to='subtitles/'),
        ),
    ]