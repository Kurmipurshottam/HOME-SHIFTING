# Generated by Django 5.0.4 on 2024-04-12 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0006_rename_contact_tcontact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TContact',
            new_name='Contact',
        ),
    ]