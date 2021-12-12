# Generated by Django 3.0.6 on 2021-12-04 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.MinLengthValidator(limit_value=2)]),
        ),
    ]
