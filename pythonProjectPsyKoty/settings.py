import os
from pathlib import Path

# Определение пути к корневой директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Быстрые настройки для разработки - не используйте в продакшн окружении
# См. https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-^q7wy2!&)%n#$0v9^7u%wr^^!$3oad2rdsrlxqu-y86me&2u9j')

DEBUG = True

ALLOWED_HOSTS = []

# Определение установленных приложений (INSTALLED_APPS)
INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_statistics',  # ваше приложение
]

# Определение промежуточного ПО (middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной файл маршрутизации URL
ROOT_URLCONF = 'pythonProjectPsyKoty.urls'

# Настройки для шаблонов (templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Убедитесь, что путь правильный
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Конфигурация WSGI приложения
WSGI_APPLICATION = 'pythonProjectPsyKoty.wsgi.application'

# Настройки базы данных (подключение к MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'my_database_psykoty'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'Oks201971'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Настройки валидаторов паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Настройки интернационализации
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Настройки для статических файлов (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Путь к статическим файлам

# Тип поля для автоинкрементных ключей по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Добавление кастомного дашборда
ADMIN_TOOLS_INDEX_DASHBOARD = 'pythonProjectPsyKoty.dashboard.CustomIndexDashboard'
