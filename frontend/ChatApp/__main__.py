''' __main__ module. '''
from PyQt5.QtWidgets import QApplication
import sys

from gui.main_window import MainWindow

APP = QApplication(sys.argv)
WINDOW = MainWindow()
sys.exit(APP.exec_())
