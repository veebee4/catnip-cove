# Generated by Django 4.2 on 2024-12-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0011_remove_donation_custom_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
