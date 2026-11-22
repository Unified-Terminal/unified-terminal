import faulthandler
faulthandler.enable()

import platform
import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from unified_terminal.window import MainWindow


def probe(label):
    from abc import ABC, abstractmethod

    class _P(ABC):
        @abstractmethod
        def f(self):
            pass

    class _Q(_P):
        def f(self):
            pass

    print(f"   probe ok na: {label}", flush=True)


def _icon_path() -> Path:
    base_path = Path(__file__).resolve().parent
    source_path = base_path.parents[1]

    paths = (
        base_path / "assets" / "UT.png",
        base_path / "assets" / "UT.ico",
        source_path / "assets" / "UT.png",
        source_path / "assets" / "UT.ico",
        Path(sys.prefix) / "share" / "unified-terminal" / "UT.png",
        Path(sys.prefix) / "share" / "unified-terminal" / "UT.ico",
    )

    for path in paths:
        if path.is_file():
            return path

    raise FileNotFoundError(
        "Unable to locate the Unified Terminal window icon."
    )


def main():
    probe("start")

    print("1: creating QApplication", flush=True)
    app = QApplication(sys.argv)
    app.setApplicationName("Unified Terminal")
    probe("QApplication")

    if platform.system() == "Windows":
        print("2: icon", flush=True)
        app.setWindowIcon(QIcon(str(_icon_path())))
        probe("icon")

    print("3: window", flush=True)
    window = MainWindow()
    probe("MainWindow")
    print("4: show", flush=True)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()