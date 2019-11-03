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
        self.tab_widget.currentChanged.connect(self.tab_selected)
        self.setCentralWidget(self.tab_widget)

    def tab_selected(self, index):
        try:
            name = self.tab_names[index-1]
            tab = self.tabs[index-1]
            import requests
            import json
            resp = requests.get(f'http://localhost:3000/api/users?name={name}')
            obj = json.loads(resp.content.decode('utf-8'))
            other_id = obj['_id']
            if int(other_id) > self.user_id:
                resp = requests.get(f'http://localhost:3000/api/conversations?user_id1={self.user_id}&user_id2={other_id}')
            else:
                resp = requests.get(f'http://localhost:3000/api/conversations?user_id1={other_id}&user_id2={self.user_id}')
            try:
                obj = json.loads(resp.content.decode('utf-8'))
                conv_id = obj['_id']
                resp = requests.get(f'http://localhost:3000/api/messages?conv_id={conv_id}')
                obj = json.loads(resp.content.decode('utf-8'))
                for msg in obj:
                    tab.message_enter.setText(msg['content'])
                    tab.send_clicked(from_here=False)
            except KeyError:
                pass
            # self.tabs[index-1].message_enter.setText('yes')
            # self.tabs[index-1].send_clicked()
            # print(self.tab_names[index-1])
        except Exception:
            pass

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
        try:
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
        except Exception:
            pass

