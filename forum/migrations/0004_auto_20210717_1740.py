# Generated by Django 3.2.4 on 2021-07-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]