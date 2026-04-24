from kittygram_backend.settings import *

# Используем SQLite для тестов вместо PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = 'test-secret-key-for-local-tests'
DEBUG = True
ALLOWED_HOSTS = ['*']
