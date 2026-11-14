import sys

from PySide6.QtWidgets import QApplication
from mediahub.ui.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)

    fenetre = MainWindow()
    fenetre.showMaximized()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
