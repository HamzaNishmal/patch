# Generated by Django 4.1.7 on 2023-03-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
