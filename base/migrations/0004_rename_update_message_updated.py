# Generated by Django 4.2.1 on 2023-06-01 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_rename_update_room_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='update',
            new_name='updated',
        ),
    ]
