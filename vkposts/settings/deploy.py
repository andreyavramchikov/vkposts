from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vkposts',
        'HOST': '',
        'USER': '',
        'PASSWORD': '',
        'CONN_MAX_AGE': 600,
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'vkposts_key_prefix'
    }
}

ALLOWED_HOSTS = ['.notknownyet.com', 'notknownyet.com.'] # subdomains and FQDN

ROOT_URLCONF = 'vkposts.urls'
