import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

if DEBUG:
    SECRET_KEY = 'django-insecure-q+qu!7t#43-d)=lb_g4q8zgs0+1^(+k08c%p*#5^pk!^@e@!!3'
    ALLOWED_HOSTS = ['localhost', "*"]
else:
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    ALLOWED_HOSTS = ['localhost', "*"]

# Application definition

INSTALLED_APPS = [
    'core',
    'channels',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'core.login_check_middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'nitincom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

LOGIN_URL = 'login_user'

WSGI_APPLICATION = 'nitincom.wsgi.application'
ASGI_APPLICATION = 'nitincom.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DB_ENGINE = os.getenv('DB_ENGINE', None)
DB_USERNAME = os.getenv('DB_USER', None)
DB_PASS = os.getenv('DB_PASSWORD', None)
DB_HOST = os.getenv('DB_HOST', None)
DB_PORT = os.getenv('DB_PORT', None)
DB_NAME = os.getenv('DB_NAME', None)
DB_NAME_TEST = os.getenv('DB_NAME', None)

if DB_ENGINE and DB_NAME and DB_USERNAME:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' + DB_ENGINE,
            'NAME': DB_NAME,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASS,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media/")

STATIC_URL="static/"
STATIC_ROOT=os.path.join(BASE_DIR,'static/')
# STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp3.netcore.co.in'
EMAIL_PORT = 587  # Port for SMTP (typically 587 for TLS)
EMAIL_USE_TLS = True  # Enable TLS (Transport Layer Security)
EMAIL_HOST_USER = 'gro@kasheemilk.com'  # Your email address
EMAIL_HOST_PASSWORD = '#GEmilk@02*'  # Your email password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Default sender email address


# configuring error log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'error.log'),  # Path to your error log file
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,  # Keep up to 5 previous log files
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
