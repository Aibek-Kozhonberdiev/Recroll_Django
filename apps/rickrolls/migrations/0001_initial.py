# Generated by Django 5.0.6 on 2024-05-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RickrollUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=5000)),
                ('number_of_transitions', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]