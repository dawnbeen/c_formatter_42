<p align="center">
  <a style="text-decoration:none" href="https://badge.fury.io/py/c-formatter-42"><img src="https://badge.fury.io/py/c-formatter-42.svg" alt="PyPI version" height="20"></a>
  <a style="text-decoration:none" href="https://github.com/cacharle/c_formatter_42/actions"><img src="https://github.com/cacharle/c_formatter_42/actions/workflows/python-package.yml/badge.svg" height="20"></a>
  <a style="text-decoration:none" href="https://github.com/cacharle/c_formatter_42/actions"><img src="https://github.com/cacharle/c_formatter_42/actions/workflows/python-publish.yml/badge.svg" height="20"></a>
  <a style="text-decoration:none" href="https://pypi.org/project/c-formatter-42/"><img src="https://img.shields.io/pypi/pyversions/c-formatter-42" height="20"></a>
</p>

<br />

<p align="center">
  <img width="65%" align="center" src="./Img/final_back.png">
</p>

# c_formatter_42

C language prettier that conforms to 42 norm v3.
I know you are already a good human norm.
It's just for convenience.

## Installation

Requires Python 3.6+ (3.7, 3.8, 3.9, 3.10)

### From PyPI

```command
$ pip3 install c-formatter-42
$ pip3 install --user c-formatter-42  # If you don't have root privileges
```

### From source

```command
$ git clone https://github.com/cacharle/c_formatter_42
$ cd c_formatter_42
$ pip3 install -e .
```

## Usage

### Command line

```command
$ c_formatter_42 < file.c
$ python3 -m c_formatter_42 < file.c  # If you get 'command not found' with the previous one

$ c_formatter_42 --help
usage: c_formatter_42 [-h] [-c] [FILE [FILE ...]]

Format C source according to the norm

positional arguments:
  FILE           File to format inplace, if no file is provided read STDIN

optional arguments:
  -h, --help     show this help message and exit
  -c, --confirm  Ask confirmation before overwritting any file
```

## Plugins / Extensions

### Vim

Check out the [`c_formatter_42.vim`](https://github.com/cacharle/c_formatter_42.vim) plugin. This plugin automatically installs the `c_formatter_42` package using pip.

### Visual Studio Code

1. Install `c_formatter_42`
1. Install the [`keyhr.42-c-format`](https://marketplace.visualstudio.com/items?itemName=keyhr.42-c-format) extension
1. Set `keyhr.42-c-format` as the default formatter for C files in `.vscode/settings.json`

```json
{
  "[c]": {
    "editor.defaultFormatter": "keyhr.42-c-format"
  }
}
```

## Contributing

Feel free to report issues or contribute. :)
