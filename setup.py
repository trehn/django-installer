from setuptools import find_packages, setup
from sys import stderr, version_info

if version_info < (2, 7):
    stderr.write("django-installer needs Python 2.7\n")
    stderr.flush()
    exit(1)


setup(
    name="django-installer",
    version="0.1.0",
    description="allows for painless installation of your Django app",
    author="Torsten Rehn",
    author_email="torsten@rehn.email",
    license="ISC",
    packages=find_packages(),
    package_data={
       'django_installer': ['installer/templates/*.html'],
    },
    url="http://github.com/trehn/django-installer",
    keywords=["django", "installer", "setup", "config", "configuration", "settings"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "Django",
    ],
    zip_safe=False,
)
