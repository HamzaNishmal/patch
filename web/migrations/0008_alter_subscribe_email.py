# Generated by Django 4.1.7 on 2023-03-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_testimonial_designation_alter_testimonial_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]