# Generated by Django 5.1.6 on 2025-02-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_bookings_user_alter_bookings_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
