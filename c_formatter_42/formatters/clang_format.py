# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    clang_format.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 10:40:07 by cacharle          #+#    #+#              #
#    Updated: 2021/02/25 20:46:18 by cacharle         ###   ########.fr        #
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
    try:
        yield
    finally:
        os.unlink(CONFIG_FILENAME)
        if previous_config is not None:
            with open(CONFIG_FILENAME, "w") as f:
                f.write(previous_config)


if sys.platform == "linux":
    CLANG_FORMAT_EXEC = os.path.join(DATA_DIR, "clang-format-linux")
elif sys.platform == "darwin":
    CLANG_FORMAT_EXEC = os.path.join(DATA_DIR, "clang-format-darwin")
elif sys.platform == "win32":
    CLANG_FORMAT_EXEC = os.path.join(DATA_DIR, "clang-format-win32.exe")
else:
    raise NotImplementedError("Your platform is not supported")


def clang_format(content: str) -> str:
    """ Wrapper around clang-format

        Pass content on stdin and return stdout.
        The clang-format executable is selected according to the platform,
        this is to keep the same version of clang-format accross all setup.
    """
    with _config_context():
        process = subprocess.Popen(
            [CLANG_FORMAT_EXEC, "-style=file"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate(input=content.encode())
        if process.returncode != 0:
            raise RuntimeError(f"clang-format error: {err.decode()}")
        return out.decode()
