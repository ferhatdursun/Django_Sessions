from .base import *

# on Live:

DEBUG = False
ALLOWED_HOSTS = [
    '127.0.0.1',
]

# LOGS:
LOGGING = { 
    "version": 1, 
    "disable_existing_loggers": True, 
    "formatters": { 
        'detail': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        },
    }, 
    "handlers": { 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "detail", 
            'filename': './prod_logs.log', 
            'level': 'INFO', 
        }, 
    }, 
    "loggers": { 
        "django": { 
            "handlers": ['file'], 
            "level": config("DJANGO_LOG_LEVEL", "INFO"), 
            'propagate': True, 
        }, 
    }, 
}


# -----------------
#   PostreSQL
#   $ pip install psycopg2 # for macOS: pip install psycopg2-binary
'''--------------
DATABASES = { 
    "default": { 
        "ENGINE": "django.db.backends.postgresql", 
        # "ENGINE": "django.db.backends.postgresql_psycopg2", 
        'NAME': 'testdb',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '3306',
        # "ATOMIC_REQUESTS": True, 
    }
}
# --------------'''


# -----------------
#   MySQL
#   $ pip install mysqlclient # for macOS after this: brew install mysql
'''--------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# --------------'''



# -----------------
#   SQLite
# '''--------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod_db.sqlite3',
    }
}
# --------------'''