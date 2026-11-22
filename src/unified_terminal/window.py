import os
import platform

from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QToolButton,
)

from unified_terminal.terminal import TerminalWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Unified Terminal")
        self.resize(1100, 700)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        add_button = QToolButton()
        add_button.setText("+")
        add_button.setAutoRaise(True)
        add_button.setToolTip("Nieuwe terminal")
        add_button.clicked.connect(self.add_terminal)
        self.tabs.setCornerWidget(add_button)

        self.setCentralWidget(self.tabs)

        self._tab_number = 0
        self.add_terminal()

        new_tab_shortcut = QShortcut(QKeySequence("Ctrl+Shift+T"), self)
        new_tab_shortcut.activated.connect(self.add_terminal)
        close_tab_shortcut = QShortcut(QKeySequence("Ctrl+Shift+W"), self)
        close_tab_shortcut.activated.connect(self.close_current_tab)

    def _create_backend(self):
        system = platform.system()

        if system == "Windows":
            from unified_terminal.windows_backend import WindowsBackend

            return WindowsBackend(), [
                "powershell.exe",
                "-NoLogo",
                "-NoExit",
                "-Command",
                "Remove-Item Alias:curl -ErrorAction SilentlyContinue",
            ]

        if system == "Linux":
            from unified_terminal.linux_backend import LinuxBackend

            shell = os.environ.get("SHELL", "/bin/bash")
            return LinuxBackend(), [shell, "-i"]

        raise RuntimeError("Unsupported operating system.")

    def add_terminal(self):
        terminal = TerminalWidget()
        backend, command = self._create_backend()
        terminal.start_backend(backend, command)
        terminal.backend_exited.connect(
            lambda terminal=terminal: self.close_tab(
                self.tabs.indexOf(terminal)
            )
        )

        self._tab_number += 1
        index = self.tabs.addTab(terminal, f"Terminal {self._tab_number}")
        self.tabs.setCurrentIndex(index)
        terminal.setFocus()

    def close_current_tab(self):
        index = self.tabs.currentIndex()
        if index >= 0:
            self.close_tab(index)

    def close_tab(self, index):
        if index < 0:
            return

        terminal = self.tabs.widget(index)
        if terminal is not None:
            if terminal.backend is not None:
                terminal.backend.close()
            terminal.deleteLater()

        self.tabs.removeTab(index)

        if self.tabs.count() == 0:
            self.close()

    def closeEvent(self, event):
        for index in range(self.tabs.count()):
            terminal = self.tabs.widget(index)
            if terminal is not None and terminal.backend is not None:
                terminal.backend.close()
        super().closeEvent(event)