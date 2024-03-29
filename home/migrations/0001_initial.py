# Generated by Django 5.0.2 on 2024-02-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('tag_image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('SKU', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('instock', models.FloatField()),
                ('available_stock', models.FloatField()),
                ('tags', models.ManyToManyField(blank=True, related_name='products', to='home.tag')),
            ],
        ),
    ]
