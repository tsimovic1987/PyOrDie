# Generated by Django 5.1.1 on 2024-09-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloDjango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='number',
            new_name='lagerort',
        ),
        migrations.AlterField(
            model_name='artikel',
            name='titel',
            field=models.CharField(max_length=8),
        ),
    ]
