# nuitka-project: --mode=standalone
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-plugin-directory={MAIN_DIRECTORY}/src/unified_terminal
# nuitka-project: --include-data-files={MAIN_DIRECTORY}/assets/UT.png=share/unified-terminal/UT.png
# nuitka-project: --include-data-files={MAIN_DIRECTORY}/assets/UT.ico=share/unified-terminal/UT.ico
# nuitka-project: --windows-console-mode=disable

# Build: python -m nuitka --windows-icon-from-ico=assets/UT.ico terminal.py

import sys
from pathlib import Path


if __name__ == "__main__":
    source_directory = Path(__file__).resolve().parent / "src"
    if source_directory.is_dir():
        sys.path.insert(0, str(source_directory))

    from unified_terminal.__main__ import main

    main()