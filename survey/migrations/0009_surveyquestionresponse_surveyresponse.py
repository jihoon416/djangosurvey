# Generated by Django 3.2.6 on 2021-08-04 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20210804_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('selected_options', models.ManyToManyField(to='survey.Option')),
                ('survey_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.surveyresponse')),
            ],
        ),
    ]
