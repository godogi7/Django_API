# Generated by Django 4.2.6 on 2023-10-31 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_is_something_wrong_question_json_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='score',
        ),
    ]
