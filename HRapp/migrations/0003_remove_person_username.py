# Generated by Django 5.0.3 on 2024-04-02 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HRapp', '0002_person_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
    ]
