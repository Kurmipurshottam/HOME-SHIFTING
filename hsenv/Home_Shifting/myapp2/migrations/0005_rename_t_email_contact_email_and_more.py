# Generated by Django 5.0.4 on 2024-04-12 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0004_rename_email_contact_t_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='t_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='t_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='t_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='t_number',
            new_name='number',
        ),
    ]
