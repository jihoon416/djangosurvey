# Generated by Django 3.2.6 on 2021-08-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20210804_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='phone_number',
            field=models.CharField(default='010-0000-0000', max_length=15),
            preserve_default=False,
        ),
    ]
