#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains DjangoKeys class.

from djangokeys.core.env_vars import EnvironmentVariables
from djangokeys.exceptions import ValueIsEmpty
from djangokeys.exceptions import ValueTypeMismatch
from djangokeys.utils import logging as logger


class DjangoKeys:
    """ Used to access values of environment variables that have been set by
        the execution environment, or are listed in an .env file.

        - environment variables specified by the .env file cannot overwrite
          environment variables set by the execution environment, unless
          `overwrite=True` when accessing the environment variable
        - the usage of a .env file is optional, so if no .env file exists at
          the specified location, the program continues silently
    """

    def __init__(self, path=".env"):
        """ Initializes a new instance of DjangoKeys.

        The usage of a .env file is optional. Therefore, if no .env file exists
        at the specified location, the program continues silently.

        :param str path: filepath to .env file containing environment vars
        """
        self._env_vars = EnvironmentVariables(path)

    def secret_key(self, key, *, overwrite=False):
        """ Access environment variable used to store value of Django's
            SECRET_KEY setting.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: str
        :returns: value of environment variable as a string

        :raises EnvironmentVariableNotFound: environment variable not set
        """
        value = self._env_vars.get_value(key, overwrite)
        if value == "":
            msg = "Environment variable '{}' cannot be empty; is secret key."
            raise ValueIsEmpty(msg.format(key))
        return value

    def str(self, key, *, overwrite=False):
        """ Access environment variable as a simple string.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: str
        :returns: value of environment variable as a string

        :raises EnvironmentVariableNotFound: environment variable not set
        """
        return self._env_vars.get_value(key, overwrite)

    def int(self, key, *, overwrite=False):
        """ Access environment variable as an integer.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: int
        :returns: value of environment variable as an integer

        :raises EnvironmentVariableNotFound: environment variable not set
        :raises ValueTypeMismatch: value cannot be interpreted as an int
        """
        value = self._env_vars.get_value(key, overwrite)
        if value == "":
            msg = "Environment variable '{}' is empty; expected int."
            raise ValueIsEmpty(msg.format(key))
        try:
            value = int(value)
        except ValueError:
            msg = "Could not interpret environment variable '{}' as int: {}"
            raise ValueTypeMismatch(msg.format(key, value))
        return value

    def float(self, key, *, overwrite=False):
        """ Access environment variable as an integer.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: int
        :returns: value of environment variable as an integer

        :raises EnvironmentVariableNotFound: environment variable not set
        :raises ValueTypeMismatch: value cannot be interpreted as an int
        """
        value = self._env_vars.get_value(key, overwrite)
        if value == "":
            msg = "Environment variable '{}' is empty; expected float."
            raise ValueIsEmpty(msg.format(key))
        try:
            value = float(value)
        except ValueError:
            msg = "Could not interpret environment variable '{}' as float: {}"
            raise ValueTypeMismatch(msg.format(key, value))
        return value

    def bool(self, key, *, overwrite=False):
        """ Access environment variable as a boolean.

        :param str key: name of environment variable
        :param bool overwrite: .env file can overwrite execution environment

        :rtype: bool
        :returns: value of environment variable as an bool

        :raises EnvironmentVariableNotFound: environment variable not set
        :raises ValueTypeMismatch: value cannot be interpreted as a bool
        """
        value = self._env_vars.get_value(key, overwrite).lower().strip()
        if value == "":
            msg = "Value of environment variable '{}' is empty, expects bool."
            raise ValueIsEmpty(msg.format(key))
        if value in ["f", "false", "0", "n", "no"]:
            return False
        if value in ["t", "true", "1", "y", "yes"]:
            return True
        msg = "Could not interpret environment variable '{}' as bool: {}"
        raise ValueTypeMismatch(msg.format(key, value))

    def report_problems(self):
        """ Reports any problems after having been used, such as unused
            environment variables specified in .env file.
        """
        # TODO: implement warnings for potential problems
        logger.warning("nothing wrong detected...")
