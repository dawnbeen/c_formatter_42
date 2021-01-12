# C formatter for 42 norminette

This is C language formatter that fits 42 norminette.
I know you are already a good Human norm.
It's just for convenience.


## Vim

Checkout [c\_formatter\_42.vim](https://github.com/cacharle/c_formatter_42.vim)



## VSCode

1. Install clang-format.

- MacOS
```
$ brew install clang-format
```
 Or you can install vscode extension `Clang-Format`


2. Copy `.clang-format` in your Workspace directory.


3. VSCode Settings
- Set Default Formatter as clang-format.
- Turn off `Format On Paste`, `Format On Save`.
- Or You can just copy this in your `.vscode/settings.json` file.
```
"editor.defaultFormatter": "xaver.clang-format",
"editor.formatOnPaste": false,
"editor.formatOnSave": false,
```
(🚨 **CAUTION**
Check your **clang-format version**.
If version is lower than 10, `SpaceBeforeSquareBrackets: false` and `AllowShortBlocksOnASingleLine: Never` can't work well.
So you should comment them out!)

4. Execute code formatting
- On Windows: Shift + Alt + F
- On Mac: Shift + Option + F
- On Linux: Ctrl + Shift + I


#### 🚨Caution(VSCode)

It's not perfect.
**You should format these rules MANUALLY after auto-formatting.**
- `global aligned`
- `declarations aligned`
- `declarations must be followed by one empty line`
- `Empty line`
```
int         aaaa = 12;
float       b = 23;
std::string ccc = 23;
```


Recommended to set in `Workspace Preference`.

Feel free to report issues or contribute. :)


## TODO

- [ ] Header file and global variable alignement
- [ ] A VSCode extension
- [ ] Atom extension 
- [ ] Sublim text extension 
