# Generated by Django 5.0.7 on 2024-07-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='image_url',
            field=models.URLField(default='https://via.placeholder.com/150'),
        ),
    ]
