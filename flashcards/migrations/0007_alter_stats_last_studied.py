# Generated by Django 4.2.5 on 2024-01-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0006_alter_stats_last_studied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='last_studied',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
