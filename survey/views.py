from django.http import HttpRequest
from django.shortcuts import render

from survey.models import Survey


def survey(request: HttpRequest, survey_id: int):
    if request.method == 'POST':
        for key, value in request.POST.lists():
            print("%s %s" % (key, value))
    selected_survey = Survey.objects.get(id=survey_id)
    return render(request, 'survey.html', {'survey': selected_survey})
