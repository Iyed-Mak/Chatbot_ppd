# Generated by Django 5.0.4 on 2024-04-28 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_users_remove_mymodel_username_mymodel_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mymodel',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
