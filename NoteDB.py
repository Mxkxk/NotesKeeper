# This Python file uses the following encoding: utf-8

import sqlite3

class NoteDB:
    def __init__(self):
        self.connect = sqlite3.connect('note.db')

    def open(self):
        if int(self.connect.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='note'").fetchall()[0][0]) == 0:
            self.connect.execute("CREATE TABLE note(name TEXT NOT NULL UNIQUE, category TEXT NOT NULL, text TEXT)")
            return [-1]
        notes = self.connect.execute("SELECT * FROM note").fetchall()
        #print(notes)
        return [0, notes]

    def save(self, name, category, text):
        notes = self.connect.execute("SELECT name FROM note").fetchall()
        name_list = [name_[0] for name_ in notes]
        if name not in name_list:
            self.connect.execute("INSERT INTO note (name, category, text) VALUES ('%s', '%s', '%s')"%(name, category, text))
        else:
            self.connect.execute("UPDATE note SET category = '%s', text = '%s' WHERE name = '%s'"%(category, text, name))
        self.connect.commit()


    def delete(self, name):
        print(self.connect.execute("DELETE FROM note WHERE name = '%s'"%(name)).fetchall())
        self.connect.commit()
