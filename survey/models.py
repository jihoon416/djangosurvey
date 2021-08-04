from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=200)


class SurveyQuestion(models.Model):
    title = models.CharField(max_length=200)

    Type = models.Choices('Type', 'SELECT RADIO CHECKBOX')
    type = models.CharField(
        max_length=200,
        choices=Type.choices,
    )

    required = models.BooleanField()

    choice_limit = models.PositiveSmallIntegerField()

    answers = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Survey(models.Model):
    questions = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
