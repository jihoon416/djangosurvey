from django.urls import path

from survey import views

urlpatterns = [
    path('survey/<int:survey_id>/', views.survey)
]
