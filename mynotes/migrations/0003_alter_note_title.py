# Generated by Django 4.0.3 on 2022-03-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0002_alter_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]