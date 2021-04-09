===============================================================================
Warnings
===============================================================================

DjangoKeys actively tries to search out misconfiguration problems, such as
type mismatches, missing or mistyped environment variables, dangerous
configuration names.

By calling the `DjangoKeys.report_problems` method after usage, DjangoKeys
will report any potential problems that it has encountered as warnings.


-------------------------------------------------------------------------------
Terminal Errors
-------------------------------------------------------------------------------

When DjangoKeys runs into a severe problem that almost definitely shouldn't
be tolerated, DjangoKeys will raise an exception that should result in the
server shutting down immediately.

* an environment variable that is completely missing
* an environment variable that is unexpectedly empty


-------------------------------------------------------------------------------
Overwritten Environment Variables
-------------------------------------------------------------------------------

When an environment variable has already been set by the execution environment,
then it probably shouldn't be overwritten by a value in `.env`.


-------------------------------------------------------------------------------
Unused Environment Variables
-------------------------------------------------------------------------------

When unused environment variables are discovered in the `.env` file.


-------------------------------------------------------------------------------
Unfiltered Secrets
-------------------------------------------------------------------------------

When Django's `DEBUG` setting is True, and an error page is served, it will
include a lot of extra information, including a list of environment variables
and their values. Django will anonymize environment variables that include one
of the following strings:

* `PASS`
* 'API'
* 'KEY'
* 'PASS'
* 'SECRET'
* 'SIGNATURE'
* 'TOKEN'

When you use DjangoKeys to access an environment variable as a secret, but its
name is not covered by this list, then a warning will be shown to inform you
that you should probably change the name of the environment variable.

source: https://docs.djangoproject.com/en/3.1/ref/settings/#debug

Although this may seem unnecessary, servers may be used as a pivot during
security breaches, and any credentials to another pivot may result in attack
propagating even further. It's a small effort, so why not do it.

.. note:

   If you want to use an allow list to specify which DEBUG variables are to
   be listed, install the following middleware: <TODO: recommendation>

