# Generated by Django 5.0.2 on 2024-02-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]