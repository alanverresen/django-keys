#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for accessing the values of environment variables.

import pytest

from unittest.mock import patch
from unittest.mock import MagicMock

from djangokeys.core.env_vars import EnvironmentVariables
from djangokeys.core.env_vars import EnvironmentVariableNotFound
from tests.files import EMPTY_ENV_PATH
from tests.files import EXAMPLE1_ENV_PATH


def test__get_value__not_found__overwrite_true():
    """ When env var isn't set, an appropriate exception is raised.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = None

        env_vars = EnvironmentVariables(EMPTY_ENV_PATH)
        with pytest.raises(EnvironmentVariableNotFound):
            env_vars.get_value("ENV_VAR", overwrite=True)
        os_mock.getenv.assert_called_once_with('ENV_VAR', None)


def test__get_value__not_found__overwrite_false():
    """ When env var isn't set, an appropriate exception is raised.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = None

        env_vars = EnvironmentVariables(EMPTY_ENV_PATH)
        with pytest.raises(EnvironmentVariableNotFound):
            env_vars.get_value("ENV_VAR", overwrite=False)
        os_mock.getenv.assert_called_once_with('ENV_VAR', None)


def test__get_value__set_by_file__overwrite_true():
    """ When env var is only set by dotenv file, use that value.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = None

        env_vars = EnvironmentVariables(EXAMPLE1_ENV_PATH)
        assert env_vars.get_value("DOMAIN", overwrite=True) == "example.org"
        os_mock.getenv.assert_called_once_with("DOMAIN", None)


def test__get_value__set_by_file__overwrite_false():
    """ When env var is only set by dotenv file, use that value.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = None

        env_vars = EnvironmentVariables(EXAMPLE1_ENV_PATH)
        assert env_vars.get_value("DOMAIN", overwrite=False) == "example.org"
        os_mock.getenv.assert_called_once_with("DOMAIN", None)


def test__get_value__set_by_environment__overwrite_true():
    """ When env var is only set by environment, use that value.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = "mydomain.org"

        env_vars = EnvironmentVariables(EMPTY_ENV_PATH)
        assert env_vars.get_value("DOMAIN", overwrite=True) == "mydomain.org"
        os_mock.getenv.assert_called_once_with("DOMAIN", None)


def test__get_value__set_by_environment__overwrite_false():
    """ When env var is only set by environment, use that value.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = "mydomain.org"

        env_vars = EnvironmentVariables(EMPTY_ENV_PATH)
        assert env_vars.get_value("DOMAIN", overwrite=False) == "mydomain.org"
        os_mock.getenv.assert_called_once_with("DOMAIN", None)


def test__get_value__conflict__overwrite_true():
    """ When env var is set by environment and dotenv file, and overwrite=True,
        then use the environment variable set by the dotenv file.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = "mydomain.org"

        env_vars = EnvironmentVariables(EXAMPLE1_ENV_PATH)
        assert env_vars.get_value("DOMAIN", overwrite=True) == "example.org"


def test__get_value__conflict__overwrite_false():
    """ When env var is set by environment and dotenv file, and overwrite=False,
        then use the environment variable set by the environment.
    """
    with patch('djangokeys.core.env_vars.os') as os_mock:
        os_mock.getenv = MagicMock()
        os_mock.getenv.return_value = "mydomain.org"

        env_vars = EnvironmentVariables(EXAMPLE1_ENV_PATH)
        assert env_vars.get_value("DOMAIN", overwrite=False) == "mydomain.org"
