from django.contrib import admin
from datetime import timedelta
from .models import VisitStatistics, QuestionStatistics, AnswerStatistics, ResponseTimeStatistics


# Класс для отображения статистики посещений с кастомным полем для общего количества посещений
@admin.register(VisitStatistics)
class VisitStatisticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'visit_time', 'page_visited', 'total_visits')

    def total_visits(self, obj):
        return VisitStatistics.objects.filter(user=obj.user).count()

    total_visits.short_description = 'Total Visits'


# Класс для отображения статистики вопросов с кастомным полем для общего количества вопросов
@admin.register(QuestionStatistics)
class QuestionStatisticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_text', 'question_time', 'total_questions')

    def total_questions(self, obj):
        return QuestionStatistics.objects.filter(user=obj.user).count()

    total_questions.short_description = 'Total Questions'


# Класс для отображения статистики ответов с кастомным полем для общего количества ответов
@admin.register(AnswerStatistics)
class AnswerStatisticsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'answer_time', 'total_answers')

    def total_answers(self, obj):
        return AnswerStatistics.objects.filter(question__user=obj.question.user).count()

    total_answers.short_description = 'Total Answers'


# Класс для отображения статистики времени ответа с кастомным полем для среднего времени ответа
@admin.register(ResponseTimeStatistics)
class ResponseTimeStatisticsAdmin(admin.ModelAdmin):
    list_display = ('question', 'response_time', 'average_response_time')

    def average_response_time(self, obj):
        times = ResponseTimeStatistics.objects.filter(question__user=obj.question.user).values_list('response_time', flat=True)
        if times:
            total_time = sum((t.total_seconds() for t in times), 0)
            average_time = timedelta(seconds=total_time / len(times))
            return average_time
        return "No data"

    average_response_time.short_description = 'Average Response Time'

