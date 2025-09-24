INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'blog',  # our custom blog app
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
