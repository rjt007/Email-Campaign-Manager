# Generated by Django 4.2.5 on 2023-09-09 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='published_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
