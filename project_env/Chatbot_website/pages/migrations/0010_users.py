# Generated by Django 5.0.4 on 2024-04-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_mymodel_delete_product_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
