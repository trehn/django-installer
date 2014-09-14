try:
    from configparser import NoSectionError, NoOptionError
except ImportError:
    from ConfigParser import NoSectionError, NoOptionError

from django import forms
from django.utils.translation import ugettext as _


def get_option(settings, section, option):
    try:
        return settings.get(section, option)
    except NoSectionError:
        return ""
    except NoOptionError:
        return ""


class BaseURLForm(forms.Form):
    title = _("Base URL")

    url = forms.URLField(
        help_text=_("The absolute URL this application will be served at."),
        initial="https://example.com",
        label=_("URL"),
    )

    def populate_from_settings(self, settings):
        self.data['url'] = get_option(settings, "base_url", "url")

    def populate_settings(self, settings):
        settings.add_section("base_url")
        settings.set("base_url", "url", self.cleaned_data['url'])


class DatabaseForm(forms.Form):
    title = _("Database")

    engine = forms.ChoiceField(
        choices=(
            ('django.db.backends.mysql', _("MySQL")),
            ('django.db.backends.oracle', _("Oracle")),
            ('django.db.backends.postgresql_psycopg2', _("Postgres")),
        ),
        initial='django.db.backends.postgresql_psycopg2',
        label=_("Engine"),
    )
    host = forms.CharField(
        initial="localhost",
        label=_("Hostname"),
        max_length=128,
    )
    name = forms.CharField(
        label=_("Database name"),
        max_length=128,
    )
    password = forms.CharField(
        label=_("Password"),
        max_length=128,
        required=False,
        widget=forms.PasswordInput,
    )
    port = forms.IntegerField(
        label=_("Port"),
        min_value=1,
        max_value=65535,
    )
    user = forms.CharField(
        label=_("Username"),
        min_length=1,
        max_length=128,
    )

    def populate_from_settings(self, settings):
        try:
            for field in ('engine', 'host', 'name', 'password', 'port', 'user'):
                self.data[field] = get_option(settings, "database", field)
        except NoSectionError:
            pass

    def populate_settings(self, settings):
        settings.add_section("database")
        for field in ('engine', 'host', 'name', 'password', 'user'):
            settings.set("database", field, self.cleaned_data[field])
        settings.set("database", "port", str(self.cleaned_data['port']))
