# Generated by Django 3.2.6 on 2021-08-04 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestionResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='option',
            name='text',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='survey',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='topic',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='type',
            field=models.CharField(choices=[('SELECT', 'select'), ('RADIO', 'radio'), ('CHECKBOX', 'checkbox')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='questions',
            field=models.ManyToManyField(to='survey.SurveyQuestion'),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey'),
        ),
        migrations.AddField(
            model_name='surveyquestionresponse',
            name='selected_options',
            field=models.ManyToManyField(to='survey.Option'),
        ),
        migrations.AddField(
            model_name='surveyquestionresponse',
            name='survey_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.surveyresponse'),
        ),
    ]
