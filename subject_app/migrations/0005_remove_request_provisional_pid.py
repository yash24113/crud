# Generated by Django 4.2.1 on 2023-09-09 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0004_request_provisional_enrollment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_provisional',
            name='pid',
        ),
    ]
