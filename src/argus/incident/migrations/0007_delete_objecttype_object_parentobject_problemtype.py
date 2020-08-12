# Generated by Django 3.0.7 on 2020-08-11 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('argus_incident', '0006_incidenttagrelation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='object',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='parent_object',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='problem_type',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='ObjectType',
        ),
        migrations.DeleteModel(
            name='ParentObject',
        ),
        migrations.DeleteModel(
            name='ProblemType',
        ),
    ]