#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains functionality to read env vars set by .env files and environment.

import os

import dotenv

from djangokeys.exceptions import EnvironmentVariableNotFound
from djangokeys.utils import logging as logger


class EnvironmentVariables:
    """ Class used to access environment variables that have been set through
        one of two ways:
            - set by execution environment
            - set by local .env file
    """

    def __init__(self, filepath):
        """ Initializes a new instance of EnvironmentVariables.
        """
        self._dotenv = _read_values_from_dotenv_file(filepath)

    def get_value(self, key, overwrite):
        """ Returns value set by a given environment variable.

        :param str key: name of environment variable
        :param bool overwrite: can .env file overwrite values of environment?

        :return: value of environment variable
        :rtype: str

        :raise EnvironmentVariableNotFound: env var not set by file/environment
        """
        v_env = os.getenv(key, None)
        v_fil = self._dotenv.get(key, None)

        if v_env is None and v_fil is None:
            msg = "Could not find an environment variable '{}'"
            raise EnvironmentVariableNotFound(msg.format(key))

        elif v_env is None:
            msg = "Using environment variable '{}' set by .env file."
            logger.info(msg.format(key))
            return v_fil

        elif v_fil is None:
            msg = "Using environment variable '{}' set by environment."
            logger.info(msg.format(key))
            return v_env

        if overwrite:
            msg = "Overwriting environment variable '{}':" \
                  "using environment variable set by .env file."
            logger.warning(msg.format(key))
            return v_fil

        else:
            msg = "Overwriting environment variable '{}' not allowed:" \
                  "using environment variable set by environment."
            logger.warning(msg.format(key))
            return v_env


def _read_values_from_dotenv_file(filepath):
    """ Reads environment variables from .env file with a given path.

    :param str filepath: path of file
    :return: dictionary containing key-value pairs listed in file
    :rtype: dict
    """
    if not os.path.exists(filepath):
        msg = "Did not find .env file at specified location: '{}'."
        logger.debug(msg.format(filepath))
        return dict()
    return dotenv.dotenv_values(filepath)
