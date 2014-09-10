try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser
from os import environ
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


__all__ = []

_config = SafeConfigParser()
_config.read(environ['DJANGO_INSTALLER_SETTINGS'])


if _config.has_section("baseurl"):
    ALLOWED_HOSTS = (urlparse(_config.get("baseurl", "url")).hostname,)
    __all__.append('ALLOWED_HOSTS')


if _config.has_section("database"):
    DATABASES = {
        'default': {
            'ENGINE': _config.get("database", "engine"),
            'HOST': _config.get("database", "host"),
            'NAME': _config.get("database", "name"),
            'PASSWORD': _config.get("database", "password"),
            'PORT': _config.get("database", "port"),
            'USER': _config.get("database", "user"),
        },
    }
    __all__.append('DATABASES')
