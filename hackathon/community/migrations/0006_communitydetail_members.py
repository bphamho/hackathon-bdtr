# Generated by Django 3.2.4 on 2021-07-17 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0005_alter_communitydetail_founder'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitydetail',
            name='members',
            field=models.ManyToManyField(related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
    ]