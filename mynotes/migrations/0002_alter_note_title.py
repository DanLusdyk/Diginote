# Generated by Django 4.0.3 on 2022-03-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]