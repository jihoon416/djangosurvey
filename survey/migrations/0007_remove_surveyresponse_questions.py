# Generated by Django 3.2.6 on 2021-08-04 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_surveyresponse_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresponse',
            name='questions',
        ),
    ]
