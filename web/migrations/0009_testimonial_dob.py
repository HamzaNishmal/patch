# Generated by Django 4.1.7 on 2023-03-11 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_subscribe_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
