# Generated by Django 4.0 on 2022-05-07 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_desc_todo_desc_rename_email_todo_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Email',
        ),
    ]
