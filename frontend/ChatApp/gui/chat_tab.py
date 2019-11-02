''' chat_tab module. '''
from PyQt5 import QtWidgets
from datetime import datetime

from .message_widget import MessageWidget

class ChatTab(QtWidgets.QWidget):
    ''' ChatTab class. '''
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.main_layout = None
        self.message_enter = None
        self.send_button = None
        self.messages_layout = None
        self.scroll = None
        self.message_widgets = list()

        self._init_ui()

    def _init_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.messages_layout = QtWidgets.QFormLayout()

        send_layout = QtWidgets.QVBoxLayout()
        self.message_enter = QtWidgets.QLineEdit() # TODO may need plaintext edit?
        self.send_button = QtWidgets.QPushButton('Send')
        self.send_button.clicked.connect(self._send_clicked)
        send_layout.addWidget(self.message_enter)
        send_layout.addWidget(self.send_button)


        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        widget = QtWidgets.QWidget(self)
        widget.setLayout(self.messages_layout)
        self.scroll.setWidget(widget)
        self.main_layout.addWidget(self.scroll)
        self.main_layout.addLayout(send_layout)
        self.setLayout(self.main_layout)

        # Add seed messages
        for i in range(100):
            self.message_enter.setText(str(i))
            self._send_clicked()

    def _send_clicked(self):
        time_str = datetime.now().strftime('%m/%d/%y %I:%M %p')
        msg_widget = MessageWidget(self.message_enter.text(), time_str, parent=self)
        self.message_widgets.append(msg_widget)
        self.messages_layout.addRow(msg_widget)
        self.message_enter.setText('')
