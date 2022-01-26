
<p align="center">
  <a style="text-decoration:none" href="https://badge.fury.io/py/c-formatter-42"><img src="https://badge.fury.io/py/c-formatter-42.svg" alt="PyPI version" height="20"></a>
  <a style="text-decoration:none" href="https://github.com/cacharle/c_formatter_42/actions"><img src="https://github.com/cacharle/c_formatter_42/actions/workflows/python-package.yml/badge.svg" height="20"></a>
   <a style="text-decoration:none" href="https://pypi.org/project/c-formatter-42/"><img src="https://img.shields.io/pypi/pyversions/c-formatter-42" height="20"></a>
</p>

<h1 align="center">
 c_formatter_42
</h1>


<p align="center">
  <img width="65%" align="center" src="./Img/final_back.png">
</p>

## What is c_formatter_42?

It is Prettier for C in 42.
I know you are already a good Human norm.
It's just for convenience.

## Installation

Requires Python3.6+ (3.7, 3.8, 3.9, 3.10)

### from pypi

```
$ pip3 install c-formatter-42
$ pip3 install --user c-formatter-42  # if you don't have root privileges
```

### from source

```
$ git clone https://github.com/cacharle/c_formatter_42
$ cd c_formatter_42
$ pip3 install -e .
```

## usage

### Vim

Checkout [c_formatter_42.vim](https://github.com/cacharle/c_formatter_42.vim) plugin. This plugin automatically installs the c_formatter_42 package using pip.

### VSCode

1. Install [emeraldwalk.runonsave](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) extension.
2. Add Configuration to vscode. (We recommend you to put it in `Workspace Preference`)

```
"emeraldwalk.runonsave": {
    "commands": [{
        "match": ".[ch]",
        "cmd": "python3 -m c_formatter_42 < ${file} | tee _cfdump && cat _cfdump | tee ${file} && rm -f _cfdump"
    }]
}
```
You can copy above and paste it in the `.vscode/setting.json`.

### Command line

```
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

Feel free to report issues or contribute. :)
