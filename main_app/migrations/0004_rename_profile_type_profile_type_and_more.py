# Generated by Django 5.0 on 2023-12-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_event_end_date_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_type',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='wedding',
        ),
        migrations.AddField(
            model_name='wedding',
            name='profiles',
            field=models.ManyToManyField(to='main_app.profile'),
        ),
    ]