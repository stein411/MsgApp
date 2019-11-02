''' main_window module. '''
from PyQt5 import QtWidgets

from .add_tab import AddTab
from .chat_tab import ChatTab

class MainWindow(QtWidgets.QMainWindow):
    ''' Main window for the chat app. '''
    def __init__(self):
        ''' Initializes a MainWindow instance and shows it. '''
        super().__init__()
        self.tab_widget = None
        self._central_widget = None
        self._layout = None
        self.add_tab = None
        self.tab_names = list()
        self.tabs = list()
        self._window_title = 'Chat App'

        self._init_ui()

        self.show()

    def _init_ui(self):
        ''' Sets up the UI. '''
        self.setWindowTitle(self._window_title)
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.add_tab = AddTab(self)
        self.tab_widget.addTab(self.add_tab, '+')
        self.setCentralWidget(self.tab_widget)

    def add_new_tab(self, user_name):
        ''' Add tab with user's name. '''
        if user_name not in self.tab_names:
            new_tab = ChatTab(self)
            self.tabs.append(new_tab)
            self.tab_names.append(user_name)
            self.tab_widget.addTab(new_tab, user_name)
        else:
            QtWidgets.QMessageBox.warning(self, self._window_title, f'Chat {user_name} exists!')
        # TODO POST to /conversations
        # add the user's json
