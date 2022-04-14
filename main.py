# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QTextEdit, QLineEdit, QPushButton, QMessageBox
from PySide2.QtCore import QFile, QIODevice, Slot, QObject
from Menu import Open, About
from NoteDB import NoteDB

class NotesKeeper(QWidget):
    def __init__(self):
        super(NotesKeeper, self).__init__()

        # set style
        styleFile = QFile("style.css")
        if styleFile.open(QIODevice.ReadOnly or QIODevice.Text):
            self.__style__ = styleFile.readAll()
            styleFile.close()
            self.__style__ = str(self.__style__).replace("\\r\\n", '').replace("\'", '')[1::]
            self.setStyleSheet(self.__style__)

        self.generate_note_ui()
        self.generate_base_form_ui()
        self.set_note_ui()

        self.note_db = NoteDB()

    def generate_note_ui(self):
        self.setWindowTitle("NoteKeeper")
        self.resize(800, 600)
        self.setMinimumSize(400, 300)
        # text line for note name
        self.setName = QLineEdit()
        self.setName.setPlaceholderText("Title of note")
        # text line for note category
        self.setCategory = QLineEdit()
        self.setCategory.setPlaceholderText("Name of category")
        # text edit for note text
        self.textEdit = QTextEdit()
        # menu buttons
        self.menu = []
        self.menu.append(QPushButton("Open"))
        self.menu.append(QPushButton("Create new"))
        self.menu.append(QPushButton("Save"))
        self.menu.append(QPushButton("Delete"))
        self.menu.append(QPushButton("About"))

        hLayoutMenu = QHBoxLayout()

        for button in self.menu:
            hLayoutMenu.addWidget(button)

        self.menu[0].clicked.connect(self.open_base_form)
        self.menu[1].clicked.connect(self.create)
        self.menu[2].clicked.connect(self.save)
        self.menu[3].clicked.connect(self.delete)
        self.menu[4].clicked.connect(self.about)

        hLayoutLines = QHBoxLayout()
        hLayoutLines.addWidget(self.setName)
        hLayoutLines.addWidget(self.setCategory)

        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, 0, 0)
        vLayout.addLayout(hLayoutMenu)
        vLayout.addLayout(hLayoutLines)
        vLayout.addWidget(self.textEdit)

        self.noteLayout = vLayout

        self.setLayout(self.noteLayout)

    def set_note_ui(self, name = None):
        self.base_form.hide()
        self.resize(self.base_form.size())
        self.move(self.base_form.pos())

        if name is not None:
            notes = self.note_db.open()
            name = name.split("\n")[0]
            if notes[0] == 0:
                for n in notes[1]:
                    if name == n[0]:
                        self.setName.setText(n[0])
                        self.setCategory.setText(n[1])
                        self.textEdit.setText(n[2])
                        break
        self.show()
        print("set_note_ui")

    def generate_base_form_ui(self):
        self.base_form = Open()
        self.base_form.button.clicked.connect(self.get_note_from_base_form)
        self.base_form.set_style(self.__style__)

    def set_base_form_ui(self):
        self.hide()
        self.base_form.put_data(self.note_db.open())
        self.base_form.resize(self.size())
        self.base_form.move(self.pos())
        self.base_form.show()

    def warning(self, title, warning):
        msgBox = QMessageBox()
        msgBox.setStyleSheet(self.__style__)
        msgBox.setWindowTitle(str(title))
        msgBox.setText(str(warning))
        msgBox.exec()

    @Slot()
    def get_note_from_base_form(self):
        if self.base_form.base_list.count() > 0 and self.base_form.base_list.currentRow() == -1:
            self.warning("WARNING!", "You haven`t choose note(")
        else:
            self.set_note_ui(self.base_form.base_list.item(self.base_form.base_list.currentRow()).text())
        print("Rows " + str(self.base_form.base_list.currentRow()))
        print("get_note_from_base_form")

    @Slot()
    def open_base_form(self):
        self.set_base_form_ui()
        print("open_base_form")

    @Slot()
    def create(self):
        msgBox = QMessageBox()
        msgBox.setStyleSheet(self.__style__)
        msgBox.setWindowTitle(" ")
        msgBox.setText("Do you want to save your note?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel);
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec()
        if ret == QMessageBox.Save:
            self.save()
        self.setName.setText("")
        self.setCategory.setText("")
        self.textEdit.setText("")
        print("Created new")

    @Slot()
    def save(self):
        correct_data = True
        if len(self.name) < 1:
            self.warning(" ", "Put some name!!!")
            correct_data = False
        if len(self.category) < 1:
            self.warning(" ", "Put some category!!!")
            correct_data = False
        if correct_data is True:
            self.note_db.save(self.name, self.category, self.text)
        print("Name: %s Cat: %s \n%s"%(self.name, self.category, self.text))

    @Slot()
    def delete(self):
        msgBox = QMessageBox()
        msgBox.setStyleSheet(self.__style__)
        msgBox.setWindowTitle(" ")
        msgBox.setText("Do you want to delete your note?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec()
        if ret == QMessageBox.Yes:
            self.note_db.delete(self.name)
            self.setName.setText("")
            self.setCategory.setText("")
            self.textEdit.setText("")
            print("Deleted")

    @Slot()
    def about(self):
        self.about_form = About()
        self.about_form.set_style(self.__style__)
        self.about_form.show()

    @property
    def name(self):
        return self.setName.text()

    @property
    def category(self):
        return self.setCategory.text()

    @property
    def text(self):
        return self.textEdit.toPlainText()

if __name__ == "__main__":
    app = QApplication([])
    widget = NotesKeeper()
    widget.show()
    sys.exit(app.exec_())
