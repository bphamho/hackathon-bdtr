# Generated by Django 3.2.5 on 2021-07-17 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor', models.CharField(max_length=200)),
                ('write_date', models.DateTimeField(verbose_name='date published')),
                ('comment', models.CharField(max_length=400)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
            ],
        ),
    ]
