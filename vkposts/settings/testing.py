from base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testing_vkposts',
        'HOST': '',
        'USER': '',
        'PASSWORD': '',
        'CONN_MAX_AGE': 600,
    }
}

TEMPLATE_LOADERS = (
    (
        'django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'testing_key_prefix'
    }
}

ALLOWED_HOSTS = ['.notknownyet.com', 'notknownyet.com.', '*.uhura.de'] # subdomains and FQDN

ROOT_URLCONF = 'vkposts.urls'