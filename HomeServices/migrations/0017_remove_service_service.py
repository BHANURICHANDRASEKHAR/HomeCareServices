# Generated by Django 3.0 on 2023-09-10 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices', '0016_auto_20230910_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service',
        ),
    ]
