# Generated by Django 5.0.4 on 2024-04-27 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
