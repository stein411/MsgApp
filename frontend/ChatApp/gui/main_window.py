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

        self.user_id = 1 # TODO get rid of this
        self.populate_chats()

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

    def populate_chats(self):
        import requests
        resp = requests.get('http://localhost:3000/api/conversations', {"user_id1": self.user_id})
        import json
        obj = json.loads(resp.content.decode('utf-8'))
        #print(obj)
        for item in obj:
            other_id = -1
            for id in item['user_ids']:
                if int(id) != self.user_id:
                    other_id = id
            if int(other_id) >= 0:
                resp = requests.get(f'http://localhost:3000/api/users?id={other_id}')
                if resp.content:
                    resp_obj = json.loads(resp.content.decode('utf-8'))
                    other_name = resp_obj['name']
                    if other_name not in self.tab_names:
                        self.add_new_tab(other_name)

