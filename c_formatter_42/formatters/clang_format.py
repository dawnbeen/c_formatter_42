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

import contextlib
import platform
import subprocess
import sys
from pathlib import Path

import c_formatter_42.data

CONFIG_FILENAME = Path(".clang-format")
DATA_DIR = Path(c_formatter_42.data.__file__).parent


@contextlib.contextmanager
def _config_context():
    """Temporarly place .clang-format config file in the current directory
    If there already is a config in the current directory, it's backed up
    then put back in place after clang-format is done running
    """
    config_path = DATA_DIR / CONFIG_FILENAME
    previous_config = None
    try:
        CONFIG_FILENAME.symlink_to(config_path)
    except FileExistsError:
        if not CONFIG_FILENAME.is_symlink():
            previous_config = CONFIG_FILENAME.read_text()
        CONFIG_FILENAME.unlink()
        CONFIG_FILENAME.symlink_to(config_path)
    try:
        yield
    finally:
        CONFIG_FILENAME.unlink()
        if previous_config is not None:
            CONFIG_FILENAME.write_text(previous_config)


if sys.platform == "linux":
    CLANG_FORMAT_EXEC = DATA_DIR / "clang-format-linux"
elif sys.platform == "darwin":
    if platform.machine() == "arm64":
        # macOS M1 or Apple Silicon
        CLANG_FORMAT_EXEC = DATA_DIR / "clang-format-darwin-arm64"
    elif platform.machine() == "x86_64":
        # macOS Intel
        CLANG_FORMAT_EXEC = DATA_DIR / "clang-format-darwin"
elif sys.platform == "win32":
    CLANG_FORMAT_EXEC = DATA_DIR / "clang-format-win32.exe"
else:
    raise NotImplementedError("Your platform is not supported")


def clang_format(content: str) -> str:
    """Wrapper around clang-format

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
        if process.returncode != 0:  # pragma: no cover
            raise RuntimeError(f"clang-format error: {err.decode()}")
        return out.decode()
