try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser
from json import load
from os import chmod, environ
from os.path import exists

from django.http import HttpResponse
from django.shortcuts import render

from . import forms

SETTING_FORMS = {
    'base_url': forms.BaseURLForm,
    'database': forms.DatabaseForm,
}


def installer(request):
    settings_file = environ['DJANGO_INSTALLER_SETTINGS']
    with open(environ["DJANGO_INSTALLER_CONFIG"]) as f:
        config = load(f)
    configured_forms = [SETTING_FORMS[setting] for setting in config['allowed_settings']]

    if request.method == 'POST':
        bound_forms = [form_class(request.POST) for form_class in configured_forms]

        all_valid = True
        for form in bound_forms:
            if not form.is_valid():
                all_valid = False
                break

        if all_valid:
            settings = SafeConfigParser()
            for form in bound_forms:
                form.populate_settings(settings)
            with open(settings_file, 'w') as f:
                chmod(settings_file, 0600)
                settings.write(f)
            return render(request, "success.html")

        context_forms = bound_forms
    else:
        context_forms = [form_class({}) for form_class in configured_forms]
        if exists(settings_file):
            settings = SafeConfigParser()
            settings.read(settings_file)
            for form in context_forms:
                form.populate_from_settings(settings)

    return render(
        request,
        "installer.html",
        {
            'forms': context_forms,
            'title': config['title'],
        }
    )
    return HttpResponse(repr(config))
