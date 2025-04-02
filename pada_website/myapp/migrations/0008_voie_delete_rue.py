# Generated by Django 5.0.4 on 2025-04-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20250401_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_voies', models.CharField(max_length=255)),
                ('quartier', models.CharField(max_length=255)),
                ('X', models.CharField(max_length=255)),
                ('Y', models.CharField(max_length=255)),
                ('qr_code', models.TextField()),
                ('description', models.CharField(max_length=255)),
                ('entites_territoriales_2', models.TextField()),
            ],
            options={
                'db_table': 'panneautage',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Rue',
        ),
    ]
