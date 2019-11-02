''' chat_tab module. '''
from PyQt5 import QtWidgets
from datetime import datetime

from .message_widget import MessageWidget

class ChatTab(QtWidgets.QWidget):
    ''' ChatTab class. '''
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self._layout = None
        self.message_enter = None
        self.send_button = None
        self.messages_layout = None
        self.message_widgets = list()

        self._init_ui()

    def _init_ui(self):
        self._layout = QtWidgets.QVBoxLayout()
        self.messages_layout = QtWidgets.QVBoxLayout()

        send_layout = QtWidgets.QVBoxLayout()
        self.message_enter = QtWidgets.QLineEdit() # TODO may need plaintext edit?
        self.send_button = QtWidgets.QPushButton('Send')
        self.send_button.clicked.connect(self._send_clicked)
        send_layout.addWidget(self.message_enter)
        send_layout.addWidget(self.send_button)

        self._layout.addLayout(self.messages_layout)
        self._layout.addLayout(send_layout)

        self.setLayout(self._layout)

    def _send_clicked(self):
        print('send clicked')
        time_str = datetime.now().strftime('%m/%d/%y %I:%M %p')
        msg_widget = MessageWidget(self.message_enter.text(), time_str, parent=self)
        self.message_widgets.append(msg_widget)
        self.messages_layout.addWidget(msg_widget)
        self.message_enter.setText('')
