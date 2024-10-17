from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserStatistics(models.Model):
    """
    Модель для хранения статистики пользователей
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью User
    questions_asked = models.IntegerField(default=0, verbose_name="Заданные вопросы")  # Количество заданных вопросов
    answers_given = models.IntegerField(default=0, verbose_name="Данные ответы")  # Количество данных ответов
    donations_made = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Пожертвования")  # Общая сумма пожертвований
    last_login = models.DateTimeField(default=timezone.now, verbose_name="Последний вход")  # Дата и время последнего входа

    def __str__(self):
        return f"Статистика пользователя {self.user.username}"

    class Meta:
        verbose_name = "Статистика пользователя"
        verbose_name_plural = "Статистика пользователей"


class VisitStatistics(models.Model):
    """
    Модель для хранения статистики посещений пользователей
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    visit_time = models.DateTimeField(default=timezone.now, verbose_name="Время посещения")
    page_visited = models.CharField(max_length=100, default='main_page', verbose_name="Страница посещения")  # Пример поля

    def __str__(self):
        return f"Посещение пользователя {self.user.username} в {self.visit_time}"

    class Meta:
        verbose_name = "Статистика посещений"
        verbose_name_plural = "Статистика посещений"


class QuestionStatistics(models.Model):
    """
    Модель для хранения статистики заданных вопросов
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    question_text = models.TextField(verbose_name="Текст вопроса")
    question_time = models.DateTimeField(default=timezone.now, verbose_name="Время вопроса")

    def __str__(self):
        return f"Вопрос пользователя {self.user.username} в {self.question_time}"

    class Meta:
        verbose_name = "Статистика вопросов"
        verbose_name_plural = "Статистика вопросов"


class AnswerStatistics(models.Model):
    """
    Модель для хранения статистики ответов на вопросы
    """
    question = models.ForeignKey(QuestionStatistics, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer_text = models.TextField(verbose_name="Текст ответа")
    answer_time = models.DateTimeField(default=timezone.now, verbose_name="Время ответа")

    def __str__(self):
        return f"Ответ на вопрос {self.question.id} в {self.answer_time}"

    class Meta:
        verbose_name = "Статистика ответов"
        verbose_name_plural = "Статистика ответов"


class ResponseTimeStatistics(models.Model):
    """
    Модель для хранения времени ответов
    """
    question = models.ForeignKey(QuestionStatistics, on_delete=models.CASCADE, verbose_name="Вопрос")
    response_time = models.DurationField(verbose_name="Время ответа")

    def __str__(self):
        return f"Время ответа на вопрос {self.question.id} - {self.response_time}"

    class Meta:
        verbose_name = "Время ответа"
        verbose_name_plural = "Время ответов"
