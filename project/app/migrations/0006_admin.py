# Generated by Django 4.2.1 on 2023-05-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_member2_complaint_rename_member1_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
            ],
        ),
    ]
