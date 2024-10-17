from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json  # Импортируйте json для работы с данными

# Главная страница
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admin/home.html')

# Дашборд
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        visit_stats = VisitStatisticsView.as_view()(request).content
        registration_stats = RegistrationStatisticsView.as_view()(request).content
        questions_stats = QuestionsStatisticsView.as_view()(request).content
        answers_stats = AnswersStatisticsView.as_view()(request).content
        response_time_stats = ResponseTimeStatisticsView.as_view()(request).content

        # Преобразуем данные из JsonResponse в словари
        visit_data = json.loads(visit_stats)
        registration_data = json.loads(registration_stats)
        questions_data = json.loads(questions_stats)
        answers_data = json.loads(answers_stats)
        response_time_data = json.loads(response_time_stats)

        context = {
            'visit_data': visit_data,
            'registration_data': registration_data,
            'questions_data': questions_data,
            'answers_data': answers_data,
            'response_time_data': response_time_data,
        }

        return render(request, 'admin/dashboard.html', context)

# Статистика посещений
class VisitStatisticsView(View):
    def get(self, request, *args, **kwargs):
        # Здесь можно добавить логику для извлечения реальных данных
        data = {
            "visit_count": 123,  # Замените на реальное значение
            "message": "Visit statistics data"
        }
        return JsonResponse(data)

# Статистика регистрации
class RegistrationStatisticsView(View):
    def get(self, request, *args, **kwargs):
        # Здесь можно добавить логику для извлечения реальных данных
        data = {
            "registration_count": 50,  # Замените на реальное значение
            "message": "Registration statistics data"
        }
        return JsonResponse(data)

# Статистика заданных вопросов
class QuestionsStatisticsView(View):
    def get(self, request, *args, **kwargs):
        # Здесь можно добавить логику для извлечения реальных данных
        data = {
            "questions_count": 25,  # Замените на реальное значение
            "message": "Questions statistics data"
        }
        return JsonResponse(data)

# Статистика ответов
class AnswersStatisticsView(View):
    def get(self, request, *args, **kwargs):
        # Здесь можно добавить логику для извлечения реальных данных
        data = {
            "answers_count": 75,  # Замените на реальное значение
            "message": "Answers statistics data"
        }
        return JsonResponse(data)

# Статистика времени ответа
class ResponseTimeStatisticsView(View):
    def get(self, request, *args, **kwargs):
        # Здесь можно добавить логику для извлечения реальных данных
        data = {
            "average_response_time": 2.5,  # Замените на реальное значение
            "message": "Response time statistics data"
        }
        return JsonResponse(data)




