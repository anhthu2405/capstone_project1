# Generated by Django 5.0.2 on 2024-03-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_friends_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='note',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
