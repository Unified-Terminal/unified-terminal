<div align="center">
  <img src="https://raw.githubusercontent.com/Unified-Terminal/unified-terminal-assets/refs/heads/master/img/banner_general.webp" alt="Unified Terminal logo" width="">
  <h1>Unified Terminal</h1>
  <p>A lightweight desktop terminal emulator for Windows and Linux.</p>
</div>

[![GPLv3](https://img.shields.io/badge/GPLv3-FFFFFF)](#) [![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#) [![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](#) [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

Unified Terminal is a Python and Qt terminal application. It uses
[pyte](https://github.com/selectel/pyte) to render terminal output and launches
the platform's shell through a pseudo-terminal backend.

## Downloads

Check the [GitHub Releases](https://github.com/Unified-Terminal/unified-terminal/releases)
page for prebuilt binaries. If no release or downloadable assets are listed,
install from source using the instructions below.

### Windows
Run the installer or the portable zip

### Linux
extract the tarball and install with the `install.sh` file, `remove.sh` is the file to remove Unified Terminal on Linux

## Features

- **Windows and Linux support** — starts PowerShell on Windows and the
  interactive shell configured in `$SHELL` on Linux (or `/bin/bash` if unset).
- **Terminal output rendering** — pyte-backed handling of ANSI colors, cursor
  movement, and screen updates.
- **Multiple terminal tabs** — open, switch, move, and close independent shell
  sessions from the tab bar.
- **Resizable terminal** — adjusts the terminal grid and shell dimensions when
  the window is resized.
- **Scrollback** — use the mouse wheel to review up to 1,000 lines of terminal
  history on Windows and Linux.
- **Copy and paste** — select text by dragging; use the keyboard shortcuts or
  right-click menu.
- **Keyboard input** — supports common control sequences, navigation keys,
  and function keys.
- **Monospace display** — prefers an installed terminal font and falls back to
  the system fixed-width font.
- **Shell lifecycle** — the application window closes when the shell exits.

Unified Terminal is under active development and does not yet implement every
feature supported by mature terminal emulators.

## Build with from source

1. Download the source code:

### Windows:
[main.zip](https://github.com/Unified-Terminal/unified-terminal/archive/refs/heads/main.zip)

### Linux:
[main.tar.gz](https://github.com/Unified-Terminal/unified-terminal/archive/refs/heads/main.tar.gz)

2. Install building toolchains:

### Windows
- Install [Python 3.13](https://www.python.org/downloads/windows/) and
  [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
- Install pip dependencies: `pip install -r requirements.txt`
- Install Nuitka for building the executable: `pip install nuitka`

#### Compile

- Compile the source code into an executable: 
```powershell
python -m nuitka --windows-icon-from-ico=assets/UT.ico terminal.py
```

### Linux
- Install [Python 3.13](https://www.python.org/downloads/source/) and
  build-essential: `sudo apt install build-essential` or `sudo dnf groupinstall "Development Tools"` depending on your distribution.
- Install pip dependencies: `pip install -r requirements.txt`
- Install Nuitka for building the executable: `pip install nuitka`
- Install patchelf for Linux: `sudo apt install patchelf` or `sudo dnf install patchelf` depending on your distribution.

#### Compile
- Compile the source code into an executable: 
```bash
python3 -m nuitka terminal.py
```

## Keyboard shortcuts

| Action | Shortcut |
| --- | --- |
| Copy selected text | `Ctrl+Shift+C` or `Ctrl+Insert` |
| Paste from clipboard | `Ctrl+Shift+V` or `Shift+Insert` |
| Open a new terminal tab | `Ctrl+Shift+T` or the `+` button |
| Close the current terminal tab | `Ctrl+Shift+W` |
| Interrupt a running command | `Ctrl+C` when no text is selected |

You can also copy or paste from the terminal's right-click menu.

## Dependencies

The runtime dependencies are declared in [`pyproject.toml`](pyproject.toml) and
listed in [`requirements.txt`](requirements.txt):

| Package | Required on | Purpose |
| --- | --- | --- |
| [PySide6](https://pypi.org/project/PySide6/) `>=6.8` | Windows and Linux | Qt desktop UI |
| [pyte](https://pypi.org/project/pyte/) `>=0.8.2` | Windows and Linux | Terminal screen and escape-sequence handling |
| [pywinpty](https://pypi.org/project/pywinpty/) `>=2.0` | Windows only | Windows pseudo-terminal backend |

The Linux backend uses Python's standard-library PTY and terminal modules.
Packaging uses setuptools.
