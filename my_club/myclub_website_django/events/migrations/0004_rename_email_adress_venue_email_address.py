# Generated by Django 4.1.5 on 2023-01-05 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='email_adress',
            new_name='email_address',
        ),
    ]