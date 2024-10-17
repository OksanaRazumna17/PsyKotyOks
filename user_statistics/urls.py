# user_statistics/urls.py
from django.urls import path
from .views import (
    HomeView,
    DashboardView,  # Імпортуємо новий перегляд
    VisitStatisticsView,
    RegistrationStatisticsView,
    QuestionsStatisticsView,
    AnswersStatisticsView,
    ResponseTimeStatisticsView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Головна сторінка
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Новий шлях для дашборду
    path('visit-statistics/', VisitStatisticsView.as_view(), name='visit_statistics'),
    path('registration-statistics/', RegistrationStatisticsView.as_view(), name='registration_statistics'),
    path('questions-statistics/', QuestionsStatisticsView.as_view(), name='questions_statistics'),
    path('answers-statistics/', AnswersStatisticsView.as_view(), name='answers_statistics'),
    path('response-time-statistics/', ResponseTimeStatisticsView.as_view(), name='response_time_statistics'),
]




