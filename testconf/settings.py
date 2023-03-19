from pathlib import Path

DJANGO_PATH = Path(__file__).resolve().parent.parent.parent
SOURCE_PATH = DJANGO_PATH.parent
SITE_PATH = SOURCE_PATH.parent


###########################################################
# Critical settings - SECRET_KEY (변경 필요) generate :
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# python3 -c 'import random; import string; print ("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + ".!@`~|[]{})(*^$#:?<>") for i in range(50)]))'
###########################################################
SECRET_KEY = 'testapp'

#############################################################
# Critical settings - DEBUG (변경 필요)
# 개발용으로만 DEBUG = True
#############################################################

DEBUG = True


###########################################################
# Critical settings - ALLOWED_HOSTS (변경 필요)
# bind될 주소를 리스트 형태로 입력.
# https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts
###########################################################

ALLOWED_HOSTS = [
    '0.0.0.0'
]


#############################################################
# Critical settings - Logging
# https://docs.djangoproject.com/en/4.1/ref/settings/#std:setting-LOGGING
#############################################################

LOG_PATH = SOURCE_PATH / 'log'
LOG_PATH.mkdir(0o755, True, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'json': {
            'format': '%(levelname)s %(asctime)s %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH / 'default.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'default': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


#############################################################
# Installed Apps
# https://docs.djangoproject.com/en/4.1/ref/settings/#installed-apps
#############################################################
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'gpp',
    'testapp',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testconf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DJANGO_PATH / 'templates']
        ,
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

WSGI_APPLICATION = 'testconf.wsgi.Application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DJANGO_PATH / 'db.sqlite3',
    },
}


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

LOCALE_PATHS = (
    (DJANGO_PATH / 'locales'),
)
LANGUAGES = [
    ('ko', 'Korean'),
    ('en', 'English'),
]

LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = 'Asia/Seoul'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

