from typing import List

from django.http import HttpRequest
from django.shortcuts import render, redirect

from survey.models import *


def survey(request: HttpRequest, survey_id: int):
    selected_survey = Survey.objects.get(id=survey_id)
    if request.method == 'POST':
        question_response_dict = {}
        survey_response = SurveyResponse(survey=selected_survey)
        for name, input_list in request.POST.lists():
            if name == 'csrfmiddlewaretoken':
                continue

            if name == 'tel':
                survey_response.phone_number = input_list[0]
                continue

            question = SurveyQuestion.objects.get(id=name)

            if len(input_list) > question.choice_limit:
                return render(request, 'survey.html', {
                    'survey': selected_survey,
                    'error': f'선택 가능한 숫자를 넘었습니다. (문항: {question.topic})',
                })
            if question.required and len(input_list) < 1:
                return render(request, 'survey.html', {
                    'survey': selected_survey,
                    'error': f'필수 선택 문항이 입력되지 않았습니다. (문항: {question.topic})',
                })

            def get_options(option_id_list: List[str]):
                return question.option_set.filter(id__in=option_id_list)

            survey_question_response = SurveyQuestionResponse(survey_response=survey_response, topic=question.topic)
            options = get_options(input_list)
            question_response_dict[question.id] = survey_question_response, options
        survey_response.save()
        for question_id in question_response_dict:
            response = question_response_dict[question_id][0]
            response.save()
            response_options = question_response_dict[question_id][1]
            response.selected_options.add(*response_options)
            response.save()
        return redirect(survey_done, survey_id=survey_id)

    else:
        return render(request, 'survey.html', {'survey': selected_survey})


def survey_done(request: HttpRequest, survey_id: int):
    selected_survey = Survey.objects.get(id=survey_id)
    return render(request, 'survey-done.html', {'survey': selected_survey})
