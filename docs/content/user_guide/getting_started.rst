===============================================================================
Getting Started
===============================================================================

-------------------------------------------------------------------------------
Simple Usage
-------------------------------------------------------------------------------

By specifying the expected type of a setting,

.. code-block:: python3

   from djangokeys import DjangoKeys
   keys = DjangoKeys("/path/to/.env")

   EMAIL_HOST = keys.url("EMAIL_HOST")
   EMAIL_PORT = keys.int("EMAIL_PORT")
   EMAIL_ADDRESS = keys.email("EMAIL_ADDRESS")
   EMAIL_PASSWORD = keys.secret("EMAIL_PASSWORD")
   EMAIL_USE_TLS = keys.bool("EMAIL_USE_TLS")

   SECRET_KEY = keys.secret_key("SECRET_KEY", auto=True)

    keys.report_problems()


-------------------------------------------------------------------------------
Generating `.env` Files
-------------------------------------------------------------------------------

After integrating djangokeys into your settings files, you can generate a
local `.env` file by running the following command:

.. code-block:: sh

   $ python3 -m djangokeys generate-env 'config.settings'

The `.env` file will be located at the file location specified in the
constructor of the DjangoKeys file. If an `.env` file is already present,
newly discovered settings are added to the end of the file as comments.


-------------------------------------------------------------------------------
Generating Secret Keys
-------------------------------------------------------------------------------

The `DjangoKeys.secret_key()` method has an exclusive parameter that can be
used to create a secret key on the fly when automatically generating a `.env`
file, or when its environment variable isn't specified.

.. code-block:: python3

   from djangokeys import DjangoKeys
   keys = DjangoKeys("/path/to/.env")

   SECRET_KEY = keys.secret_key("SECRET_KEY", auto=DEBUG)

This package also features a CLI tool to manually generate a tool:

.. code-block :: sh

    $ python3 -m djangokeys generate-key --length 128
