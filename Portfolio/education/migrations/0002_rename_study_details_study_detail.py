# Generated by Django 4.1.3 on 2022-11-14 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='study_details',
            new_name='study_detail',
        ),
    ]