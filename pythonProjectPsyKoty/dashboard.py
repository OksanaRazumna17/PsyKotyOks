# dashboard.py
from admin_tools.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):
    """
    Кастомный дашборд для главной страницы админки.
    """
    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            title='User Statistics',
            models=[
                'user_statistics.models.VisitStatistics',
                'user_statistics.models.QuestionStatistics',
                'user_statistics.models.AnswerStatistics',
                'user_statistics.models.ResponseTimeStatistics',
            ],
        ))

        self.children.append(modules.RecentActions(
            title='Recent Actions',
            limit=5
        ))

        self.children.append(modules.LinkList(
            title='Important Links',
            children=[
                {
                    'title': 'Django Documentation',
                    'url': 'https://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': 'Python Website',
                    'url': 'https://www.python.org/',
                    'external': True,
                }
            ]
        ))
