# Generated by Django 3.2.6 on 2022-03-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("argus_notificationprofile", "0008_remove_media_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationprofile", name="timeslot_copy", field=models.IntegerField(null=True)
        ),
        migrations.AlterField(
            model_name="notificationprofile",
            name="timeslot",
            field=models.AutoField(
                primary_key=True,
            ),
        ),
        migrations.RenameField(
            model_name="notificationprofile",
            old_name="timeslot",
            new_name="id",
        ),
        migrations.AddField(
            model_name="notificationprofile",
            name="timeslot",
            field=models.ForeignKey(
                null=True,
                on_delete=models.deletion.CASCADE,
                related_name="notification_profiles",
                to="argus_notificationprofile.timeslot",
            ),
        ),
        migrations.AddField(
            model_name="notificationprofile",
            name="name",
            field=models.CharField(
                blank=True,
                max_length=40,
                null=True,
            ),
        ),
        migrations.AddConstraint(
            model_name="notificationprofile",
            constraint=models.UniqueConstraint(fields=("user", "name"), name="unique_name_per_user"),
        ),
    ]