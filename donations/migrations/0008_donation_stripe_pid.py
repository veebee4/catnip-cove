# Generated by Django 5.1.3 on 2024-11-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0007_donation_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='stripe_pid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]