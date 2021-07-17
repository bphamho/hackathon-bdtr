# Generated by Django 3.2.4 on 2021-07-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='videos/%y')),
                ('post_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
