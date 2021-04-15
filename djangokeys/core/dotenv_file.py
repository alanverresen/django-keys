import os

import dotenv

from djangokeys.utils import logging as logger


def read_values_from_dotenv_file(filepath):
    """ Reads environment variables from .env file with a given path.
        If the file doesn't exist yet, an empty dictionary is returned.

    :param str filepath: path of file
    :return: dictionary containing key-value pairs listed in file
    :rtype: dict
    """
    if not os.path.exists(filepath):
        msg = "Did not find .env file at specified location: '{}'."
        logger.debug(msg.format(filepath))
        return dict()
    return dotenv.dotenv_values(filepath)


def write_values_to_dotenv_file(filepath, env_vars):
    """ Writes environment variables to .env file with a given path.
        If the file already exists, its contents are cleared.
    """
    with open(filepath, 'w') as f:
        for key, value in env_vars.items():
            f.write("{}={}\n".format(key, value))
