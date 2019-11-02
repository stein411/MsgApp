''' add_tab module. '''
from PyQt5 import QtWidgets


class AddTab(QtWidgets.QWidget):
    ''' Add tab class. '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._layout = None
        self.users_name = None
        self.add_chat_btn = None
    
        self._init_ui()

    def _init_ui(self):
        self._layout = QtWidgets.QVBoxLayout()
        self.users_name = QtWidgets.QLineEdit()
        self.users_name.setPlaceholderText('Username')
        
        self.add_chat_btn = QtWidgets.QPushButton('Add Chat')
        self.add_chat_btn.clicked.connect(self._add_tab_clicked)

        self._layout.addWidget(self.users_name)
        self._layout.addWidget(self.add_chat_btn)

        self.setLayout(self._layout)

    def _add_tab_clicked(self):
        self.parent.add_new_tab(self.users_name.text())
