# Generated by Django 2.2.10 on 2020-02-06 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='choice_text',
        ),
    ]
