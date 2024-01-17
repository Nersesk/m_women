import os
from pathlib import Path
import environ
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=['localhost', '127.0.0.1'])

SMTP_SERVER = env.str('SMTP_SERVER', default='')
SMTP_PORT = env.str('SMTP_PORT', default='')
SMTP_USERNAME = env.str('SMTP_USERNAME', default='')
SMTP_PASSWORD = env.str('SMTP_PASSWORD', default='')
MAIL_FROM = env.str('MAIL_FROM_ADDRESS', default='')
MAIL_TO = env.str('MAIL_TO', default='')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'ckeditor',
    'image_uploader_widget',
    'solo'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n'
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {

    'default': {
        'ENGINE': env.str('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME':  env.str('DB_NAME', default=''),
        'USER':  env.str('DB_USERNAME', default=''),
        'PASSWORD':  env.str('DB_PASSWORD', default=''),
        'HOST':  env.str('DB_HOST', default=''),
        'PORT':  env.str('DB_PORT', default=''),

    }

}

# # local set
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
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

LANGUAGE_CODE = 'en'


LANGUAGES = [
    ('hy', 'Armenian'),
    ('en', 'English'),  # Example: English
]
TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True

USE_TZ = True


STATIC_URL = env.str('STATIC_URL', default='static/')
MEDIA_URL = env.str('MEDIA_URL', default='/media/')
STATIC_ROOT = env.str('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = env.str('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']

        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
                    'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       ]},

            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText','PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'links', 'items': ['Link', 'Unlink',]},
            {'name': 'insert',
             'items': ['HorizontalRule', 'Smiley', 'SpecialChar',]},
            {'name': 'yourcustomtools', 'items': [
                'Print',
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here

        'tabSpaces': 4,
        'removePlugins': 'image',
    }
}
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#translations path
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'core', 'locale'),
]