# Generated by Django 5.0.7 on 2024-07-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(max_length=250)),
                ('nom_rue', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('quartier', models.CharField(max_length=250)),
            ],
        ),
    ]
