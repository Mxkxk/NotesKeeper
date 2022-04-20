# This Python file uses the following encoding: utf-8
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QGridLayout, QLabel, QSizePolicy
from PySide2.QtCore import Qt

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
        self.setMaximumSize(800, 450)
        self.setMinimumSize(800, 450)
        gl = QGridLayout()

        labelAbout = QLabel("NoteKeeper")
        descr = QLabel("NoteKeeper - is modern way to keep and edit your own notes. Use it as u want///")
        descr.setWordWrap(True)
        date = QLabel('2022, Maksym Fedoriak\nmaksim.fedoryak@gmail.com\nTg:@mox_em')

        wid = QWidget()
        wid.setStyleSheet("background: url(nk.png);background-repeat:no-repeat;");

        gl.addWidget(wid, 0, 0, 5, 3)
        gl.addWidget(labelAbout, 0, 2)
        gl.addWidget(descr, 1, 2, 3, 1, Qt.AlignTop)
        gl.addWidget(date, 4, 2)

        self.setLayout(gl)

    def set_style(self, style):
        if style is not None:
            self.setStyleSheet(style)
