# Generated by Django 3.1 on 2021-06-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_color', models.CharField(max_length=20)),
            ],
        ),
    ]
