# Generated by Django 4.2.5 on 2024-01-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0007_alter_stats_last_studied'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='need_practice_cards',
            field=models.IntegerField(default=0),
        ),
    ]
