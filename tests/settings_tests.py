try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser
from os import environ
from tempfile import NamedTemporaryFile
from unittest import TestCase


IMPORT_MAGIC = """
import sys
try:
    del sys.modules["django_installer.settings"]
except KeyError:
    pass
from django_installer.settings import *
"""
IMPORTED_GLOBALS = ['__builtins__', 'sys']


class BaseURLTest(TestCase):
    def test_base_url(self):
        tmpfile = NamedTemporaryFile()

        config = SafeConfigParser()
        config.add_section("baseurl")
        config.set("baseurl", "url", "https://www.example.com/foo")
        config.write(tmpfile)
        tmpfile.flush()

        environ["DJANGO_INSTALLER_SETTINGS"] = tmpfile.name
        env = {}
        exec(IMPORT_MAGIC, env)

        self.assertEqual(env.keys(), IMPORTED_GLOBALS + ['ALLOWED_HOSTS'])
        self.assertEqual(env['ALLOWED_HOSTS'], ("www.example.com",))


class DatabaseTest(TestCase):
    def test_database(self):
        tmpfile = NamedTemporaryFile()

        config = SafeConfigParser()
        config.add_section("database")
        config.set("database", "engine", "django.db.backends.mysql")
        config.set("database", "host", "db.example.com")
        config.set("database", "name", "example")
        config.set("database", "password", "secret")
        config.set("database", "port", "3306")
        config.set("database", "user", "jdoe")
        config.write(tmpfile)
        tmpfile.flush()

        environ["DJANGO_INSTALLER_SETTINGS"] = tmpfile.name
        env = {}
        exec(IMPORT_MAGIC, env)

        self.assertEqual(env.keys(), IMPORTED_GLOBALS + ['DATABASES'])
        self.assertEqual(env['DATABASES'], {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'example',
                'HOST': 'db.example.com',
                'USER': 'jdoe',
                'PASSWORD': 'secret',
                'PORT': '3306',
            }
        })
