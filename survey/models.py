from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)

    TYPE_CHOICES = (
        ('SELECT', 'select'),
        ('RADIO', 'radio'),
        ('CHECKBOX', 'checkbox'),
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
    )

    required = models.BooleanField()

    choice_limit = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.topic


class Option(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.survey.title + ' 응답 결과 #' + str(self.id)


class SurveyQuestionResponse(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    selected_options = models.ManyToManyField(Option)

    def __str__(self):
        return self.topic
