# Generated by Django 2.2.6 on 2019-11-03 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_new_publish_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='News',
        ),
    ]
