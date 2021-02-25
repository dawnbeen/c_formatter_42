# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    clang_format.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 10:40:07 by cacharle          #+#    #+#              #
#    Updated: 2021/02/25 19:13:06 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import os
import sys
import inspect
import subprocess
from contextlib import contextmanager

import c_formatter_42.data

CONFIG_FILENAME = ".clang-format"

DATA_DIR = os.path.dirname(inspect.getfile(c_formatter_42.data))


@contextmanager
def _config_context():
    """ Temporarly place .clang-format config file in the current directory
        If there already is a config in the current directory, it's backed up
        then put back in place after clang-format is done running
    """
    config_path = os.path.join(DATA_DIR, CONFIG_FILENAME)
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


if sys.platform == "linux":
    CLANG_FORMAT_EXEC = os.path.join(DATA_DIR, "clang-format-linux")
elif sys.platform == "darwin":
    CLANG_FORMAT_EXEC = os.path.join(DATA_DIR, "clang-format-darwin")
else:
    raise NotImplementedError("Your platform is not supported")


def clang_format(content: str) -> str:
    """ Wrapper around the clang-format command

        Pass content on stdin and return stdout

        Note:
            Need to put .clang-format in user's home directory
            since clang-format doesn't allow to specify
            the path to a configuration file
    """
    with _config_context():
        print(CLANG_FORMAT_EXEC)
        process = subprocess.Popen(
            [CLANG_FORMAT_EXEC, "-style=file"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate(input=content.encode())
        print("code", process.returncode)
        print("stderr: ", err.decode())
        return out.decode()
