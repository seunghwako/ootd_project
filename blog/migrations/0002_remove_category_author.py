# Generated by Django 3.0.3 on 2020-03-20 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
    ]
