import sys
from app import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def _init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    qt.exec()