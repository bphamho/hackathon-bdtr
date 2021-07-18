# Generated by Django 3.2.5 on 2021-07-17 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20210718_0004'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0006_communitydetail_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitydetail',
            name='posts',
            field=models.ManyToManyField(related_name='community_posts', to='forum.Post'),
        ),
        migrations.AlterField(
            model_name='communitydetail',
            name='image',
            field=models.ImageField(default='no_image.png', upload_to='images/community'),
        ),
        migrations.AlterField(
            model_name='communitydetail',
            name='members',
            field=models.ManyToManyField(related_name='community_members', to=settings.AUTH_USER_MODEL),
        ),
    ]