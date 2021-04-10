===============================================================================
Introduction
===============================================================================

-------------------------------------------------------------------------------
What is django-keys?
-------------------------------------------------------------------------------

**django-keys** is a Python package used for handling Django's secrets and
settings in a secure and portable way:

* reads secrets from configuration files and environment variables
* checks settings for common problems and irregularities
* generate local `.env` files to specify environment variables
* generate secure SECRET_KEY values
* CLI tools to get started as fast as possible


-------------------------------------------------------------------------------
Motivation
-------------------------------------------------------------------------------

Secrets shouldn't be hardcoded or committed to a code repository. Whenever a
change containing a secret is committed to a code repository, it may result in
a security breach, now or in the future. Although removing a secret from a code
repository's history is possible, it may take a lot of effort, and the secret
may already have been compromised and abused by an attacker by the time that it
is removed and replaced. Therefore, it is important that secrets are never
committed to a code repository in the first place.

A typical Django project involves one of two types of secrets:

* Django's SECRET_KEY setting
* private keys used to consume third-party services

On top of managing several secrets, Django projects typically also have to
manage various configuration settings that depend on the environments that
they are deployed in. For example, the DATABASES setting used by developers,
or in test environments, is likely to be different from the DATABASES setting
used in production environments.

**django-keys** provides a unified approach to handle all of these problems in
a clean and secure way that is easy to manage.


-------------------------------------------------------------------------------
Approaches
-------------------------------------------------------------------------------

There are two general approaches to handling secrets and configuration settings
in Django applications, so that secrets don't have to be hardcoded and
committed to code repositories:

* using environment variables to access secrets
* reading secrets from files that are kept out of version control system

There is no right answer to which approach is best, as each approach comes with
several advantages and disadvantages. Using an approach based on using
environment variables is recommended by the authors of the twelve-factor app
methodology (https://www.12factor.net/config), although they do acknowledge
that the second approach can work as well.

Tools that are used to configure execution environments universally support
setting specific environment variables, but usually do this through a startup
script, an out-of-source tool-specific configuration file, a web interface,
etc. On the other hand, files are drag-and-drop portable, and allow you to use
any (supported) format, but there's always the risk of accidentally committing
the configuration file to a code repository.

Several mature Python packages that are commonly used to specify Django's
configuration settings already exist:

* dotenv (https://pypi.org/project/python-dotenv/)
* django-environ (https://pypi.org/project/django-environ/)

Both allow you to use environment variables to configure your Django web
project, but also allow you to use a local file called `.env` to specify or
overwrite environment variables. This `.env` file is kept out of your
version control system, and is kept locally in each environment instead.
This really is the best of both worlds.

.. note::
   I would actually advise against using `django-environ`, because it parses
   `.env` files in a non-standard way, resulting in unexpected/weird errors
   that might be hard to understand or resolve.


-------------------------------------------------------------------------------
Why django-keys?
-------------------------------------------------------------------------------

**WARNING: These promises are still in development.**

Although using any of the aforementioned packages is fine, neither seems to
be an ideal tool to use for Django specifically. Besides reading additional
environment variables from a `.env` file, **django-keys** promises to do more
and do it better:

* builds `.env` files automatically based on your settings file
* alert users when potential security problems are detected
* supports other file formats besides `.env` files for storing keys (JSON, YAML)
* direct support for secrets management services

It's the fully integrated solution for managing keys in Django projects.

https://docs.djangoproject.com/en/dev/howto/deployment/checklist/#secret-key
https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
