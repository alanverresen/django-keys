===============================================================================
Getting Started
===============================================================================

-------------------------------------------------------------------------------
Simple Usage
-------------------------------------------------------------------------------

The easiest way to integrate **django-keys**, is by creating a DjangoKeys
application at the start of your settings file. When creating a DjangoKeys
instance, you have to pass the filepath of an existing *.env* file as its
only argument.

.. code-block:: python3

   from djangokeys import DjangoKeys

   keys = DjangoKeys("/path/to/.env")

   EMAIL_HOST = keys.str("EMAIL_HOST")
   EMAIL_PORT = keys.int("EMAIL_PORT")
   EMAIL_ADDRESS = keys.str("EMAIL_ADDRESS")
   EMAIL_PASSWORD = keys.str("EMAIL_PASSWORD", secret=True)
   EMAIL_USE_TLS = keys.bool("EMAIL_USE_TLS")

   SECRET_KEY = keys.secret_key("SECRET_KEY")

   keys.report_problems()

At the end of the settings file, you can call the `report_problems` method
to report potential problems, such as unused environment variables that were
set by the '.env' file.


-------------------------------------------------------------------------------
Generating `.env` Files
-------------------------------------------------------------------------------

**WARNING: This functionality hasn't been implemented yet!**

If you don't want to write your own `.env` file, you can generate a local
`.env` file by running the following command after integrating djangokeys
into your settings files, and pointing the tool towards your settings file:

.. code-block:: sh

   $ python3 -m djangokeys generate-env 'config.settings'

The `.env` file will be located at the file location that was provided to the
DjangoKeys instance. You can generate a secret key for Django's SECRET_KEY
using the CLI tool discussed below, or provide the `--generate-secret-key`
flag to automatically generate the secret key while building .

.. code-block:: sh

   $ python3 -m djangokeys generate-env 'config.settings' --generate-secret-key

If an `.env` file is already present, then all newly discovered settings will
be added to the end of the file as comments.


-------------------------------------------------------------------------------
Generating Secret Keys
-------------------------------------------------------------------------------

As discussed earlier, this package also features a CLI tool to manually
generate a secret key of a given length:

.. code-block:: sh

    $ python3 -m djangokeys generate-key --length 128
