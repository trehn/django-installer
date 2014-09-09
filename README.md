django-installer provides helpers for installing Django-based apps without the need to mess with Django config files. It provides a tiny web application for selecting a database for your main application to use, along with various other settings.

When using django-installer, installing and configuring your Django app can look like this:

```
pip install yourapp
yourapp-setup
# go to http://127.0.0.1:8080 and enter database credentials in web form
yourapp-start
```

To use django-installer with your app, you just need to do the following:

1. add django-installer to the dependencies of your app

2. at the bottom of your generic `settings.py`, add this:

```python
from django_installer.settings import *
```

3. anywhere in your app, define a function like this:

```python
from django_installer import run_installer

def installer():
	run_installer(
		allowed_settings=['base_url', 'database'],
		settings_path="/etc/yourapp.conf",
	)
```

4. add that function to your `setup.py` as a script:

```python
setup(
    [...]
    entry_points={
        'console_scripts': [
            "yourapp-setup=yourapp.dotted.module.path:installer",
        ],
    },
)
```
