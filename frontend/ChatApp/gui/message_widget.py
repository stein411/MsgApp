''' message_widget module. '''
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class MessageWidget(QtWidgets.QWidget):
    ''' Message widget class. '''
    def __init__(self, message_txt='', time='', parent=None):
        super().__init__(parent)
        self._layout = None
        self.message_content = None
        self.timestamp = None
        self.time_str = time
        self._message_txt = message_txt

        self._init_ui()

    def _init_ui(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.green)
        self.setPalette(palette)
        self._layout = QtWidgets.QVBoxLayout()

        self.timestamp = QtWidgets.QLabel(self.time_str)
        self.message_content = QtWidgets.QLabel(self._message_txt)

        self._layout.addWidget(self.timestamp)
        self._layout.addWidget(self.message_content)
        self.setLayout(self._layout)
