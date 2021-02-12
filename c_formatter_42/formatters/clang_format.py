# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    clang_format.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 10:40:07 by cacharle          #+#    #+#              #
#    Updated: 2021/02/12 11:38:45 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import os
import sys
import subprocess
from contextlib import contextmanager

import c_formatter_42

if sys.version_info >= (3, 7):
    from importlib.resources import path as resources_path
else:
    from importlib_resources import path as resources_path

CONFIG_FILENAME = ".clang-format"


@contextmanager
def _config_context():
    """ Temporarly place .clang-format config file in the current directory
        If there already is a config in the current directory, it's backed up
        then put back in place after clang-format is done running
    """
    with resources_path(c_formatter_42, CONFIG_FILENAME) as config_path:
        previous_config = None
        try:
            os.symlink(config_path, CONFIG_FILENAME)
        except FileExistsError:
            if not os.path.islink(CONFIG_FILENAME):
                with open(CONFIG_FILENAME) as f:
                    previous_config = f.read()
            os.unlink(CONFIG_FILENAME)
            os.symlink(config_path, CONFIG_FILENAME)
        yield
        os.unlink(CONFIG_FILENAME)
        if previous_config is not None:
            with open(CONFIG_FILENAME, "w") as f:
                f.write(previous_config)


def clang_format(content: str) -> str:
    """ Wrapper around the clang-format command

        Pass content on stdin and return stdout

        Note:
            Need to put .clang-format in user's home directory
            since clang-format doesn't allow to specify
            the path to a configuration file
    """
    with _config_context():
        process = subprocess.Popen(
            ["clang-format", "-style=file"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        out, _ = process.communicate(input=content.encode())
        return out.decode()
