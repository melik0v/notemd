# Generated by Django 4.2.5 on 2023-10-06 07:35

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
