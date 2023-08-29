# Generated by Django 4.2.1 on 2023-08-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0003_programmes_semesters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('cource_id', models.AutoField(db_column='cource_id', primary_key=True, serialize=False)),
                ('cource_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cource_master',
            },
        ),
    ]