from json import dump
from os import environ
from os.path import expanduser
from sys import argv
from tempfile import NamedTemporaryFile

from django.core.management import execute_from_command_line


def run_installer(title, allowed_settings=None, settings_path="/etc/django.conf"):
    if allowed_settings is None:
        allowed_settings = ['base_url', 'database']

    config = {
        'title': title,
        'allowed_settings': allowed_settings,
    }

    config_file = NamedTemporaryFile()
    dump(config, config_file)
    config_file.flush()

    environ["DJANGO_INSTALLER_CONFIG"] = config_file.name
    environ["DJANGO_INSTALLER_SETTINGS"] = expanduser(settings_path)

    execute_from_command_line([
        argv[0],
        "runserver",
        #"--noreload",
        "--settings=django_installer.installer.settings",
    ] + argv[1:])
