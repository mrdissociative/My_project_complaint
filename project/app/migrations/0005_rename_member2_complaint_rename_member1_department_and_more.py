# Generated by Django 4.2.1 on 2023-05-11 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_member1_date_member_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member2',
            new_name='Complaint',
        ),
        migrations.RenameModel(
            old_name='Member1',
            new_name='Department',
        ),
        migrations.RenameModel(
            old_name='Member',
            new_name='User',
        ),
    ]
