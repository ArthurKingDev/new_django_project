# Generated by Django 4.1.2 on 2022-11-17 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_id',
            new_name='artiste_id',
        ),
    ]
