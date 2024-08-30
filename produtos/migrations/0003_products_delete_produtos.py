# Generated by Django 5.1 on 2024-08-30 16:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_rename_manufacturer_produtos_mark_produtos_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]
