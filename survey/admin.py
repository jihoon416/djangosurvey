from django.contrib import admin

from survey.models import *


class SurveyQuestionOptionInline(admin.StackedInline):
    model = Option
    extra = 1


class SurveyQuestionInline(admin.StackedInline):
    model = SurveyQuestion
    extra = 1
    show_change_link = True


class SurveyResponseInline(admin.StackedInline):
    model = SurveyResponse
    extra = 0
    show_change_link = True


class SurveyAdmin(admin.ModelAdmin):
    inlines = [
        SurveyQuestionInline,
        SurveyResponseInline,
    ]


admin.site.register(Survey, SurveyAdmin)


class SurveyQuestionAdmin(admin.ModelAdmin):
    inlines = [SurveyQuestionOptionInline]


admin.site.register(SurveyQuestion, SurveyQuestionAdmin)


class SurveyQuestionResponseInline(admin.TabularInline):
    model = SurveyQuestionResponse
    extra = 0


class SurveyResponseAdmin(admin.ModelAdmin):
    inlines = [SurveyQuestionResponseInline]


admin.site.register(SurveyResponse, SurveyResponseAdmin)
