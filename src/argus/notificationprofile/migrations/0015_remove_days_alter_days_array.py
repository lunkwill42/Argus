# Generated by Django 4.1.7 on 2024-01-31 13:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("argus_notificationprofile", "0014_timerecurrence_days_array"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timerecurrence",
            name="days",
        ),
        migrations.RenameField(
            model_name="timerecurrence",
            old_name="days_array",
            new_name="days",
        ),
    ]