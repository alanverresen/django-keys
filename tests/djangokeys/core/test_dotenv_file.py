#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Contains tests for reading environment variables from .env file.

from os.path import join as path_join
from tempfile import TemporaryDirectory

from djangokeys.core.dotenv_file import read_values_from_dotenv_file
from djangokeys.core.dotenv_file import write_values_to_dotenv_file

from tests.files import EXAMPLE1_ENV_PATH
from tests.utils.environment_vars import use_environment_variable


def test__read_values_from_dotenv__file_does_not_exist():
    """ Tests that an empty directory is returned when .env doesn't exist.
    """
    values = read_values_from_dotenv_file("does_not_exist.env")
    assert type(values) == dict
    assert len(values) == 0


def test__read_values_from_dotenv__file_exists():
    """ Tests that values are successfully read from file.
    """
    values = read_values_from_dotenv_file(EXAMPLE1_ENV_PATH)
    assert values["DOMAIN"] == "example.org"
    assert values["ADMIN_EMAIL"] == "admin@example.org"
    assert values["ROOT_URL"] == "example.org/app"
    assert values["HELLO"] == "nobody answers back"


def test__read_values_from_dotenv__cant_read_execution_environment():
    """ Environment variables set by execution environment aren't accessed.
    """
    with use_environment_variable('EV_123', 'value'):
        values = read_values_from_dotenv_file(EXAMPLE1_ENV_PATH)
        assert 'EV_123' not in values


def test__write_values_to_dotenv__file():
    """
    """
    with TemporaryDirectory() as dir_path:
        filepath = path_join(dir_path, ".env")
        env_vars = {"VAR_A": "a", "VAR_B": "", "VAR_C": "5"}
        write_values_to_dotenv_file(filepath, env_vars)

        with open(filepath, 'r') as f:
            lines = f.readlines()

    assert len(lines) == 3
    assert "VAR_A=a\n" in lines
    assert "VAR_B=\n" in lines
    assert "VAR_C=5\n" in lines
