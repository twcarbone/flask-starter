# githooks
Git hooks to be used with your projects.

Clone this repository as a submodule into base project.
```shell
$ git submodule add git@github.com:tcarbone073/.githooks.git
```

Configure the git hooks path by editing `.git/config`
```shell
[core]
    hooksPath = .githooks
```

Or run `git config`
```shell
$ git config --global core.hooksPath .githooks
```

Ensure any hook is executable.
```shell
$ chmod 755 pre-commit
```

On Windows, `chmod` will not work. A proper `shebang` makes the file executale.
```shell
#!/bin/bash; C:/Program\ Files/Git/usr/bin/sh.exe
```