# Generated by Django 4.2.4 on 2023-08-21 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GDF', '0002_userinput_delete_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInput',
            new_name='Questions',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='input_text',
            new_name='name',
        ),
    ]
