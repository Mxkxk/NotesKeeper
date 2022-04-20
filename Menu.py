# This Python file uses the following encoding: utf-8
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget

class Open(QWidget):
    def __init__(self):
        super(Open, self).__init__()
        self.setWindowTitle("NoteKeeper - Choose Note")
        self.setWindowIcon(QIcon("nk_ico.png"))
        print(QIcon("nk_ico.png"))

        self.id_ = 0
        vLayout = QVBoxLayout()
        vLayout.setSpacing(0)
        vLayout.setContentsMargins(0, 0, 0, 0)

        self.button = QPushButton("Choose")

        self.base_list = QListWidget()

        vLayout.addWidget(self.button)
        vLayout.addWidget(self.base_list)
        self.setLayout(vLayout)

        self.resize(800, 600)
        self.setMinimumSize(400, 300)

    def set_style(self, style):
        if style is not None:
            self.setStyleSheet(style)

    def put_data(self, data):
        if data[0] == 0:
            #print(data)
            data = data[1]
            self.base_list.clear()
            for n in data:
                self.base_list.addItem(n[0]+"\n"+n[1])

class About(QWidget):
    def __init__(self):
        super(About, self).__init__()
        self.setWindowTitle("NoteKeeper - About")
        self.setWindowIcon(QIcon("nk_ico.png"))
        self.resize(800, 600)
        self.setMinimumSize(400, 300)

    def set_style(self, style):
        if style is not None:
            self.setStyleSheet(style)
