/********************************************************************************
** Form generated from reading UI file 'form.ui'
**
** Created by: Qt User Interface Compiler version 5.12.11
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FORM_H
#define UI_FORM_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_NotesKeeper
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *NotesKeeper)
    {
        if (NotesKeeper->objectName().isEmpty())
            NotesKeeper->setObjectName(QString::fromUtf8("NotesKeeper"));
        NotesKeeper->resize(800, 600);
        centralwidget = new QWidget(NotesKeeper);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(10, 10, 221, 101));
        NotesKeeper->setCentralWidget(centralwidget);
        menubar = new QMenuBar(NotesKeeper);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 20));
        NotesKeeper->setMenuBar(menubar);
        statusbar = new QStatusBar(NotesKeeper);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        NotesKeeper->setStatusBar(statusbar);

        retranslateUi(NotesKeeper);

        QMetaObject::connectSlotsByName(NotesKeeper);
    } // setupUi

    void retranslateUi(QMainWindow *NotesKeeper)
    {
        NotesKeeper->setWindowTitle(QApplication::translate("NotesKeeper", "NotesKeeper", nullptr));
        pushButton->setText(QApplication::translate("NotesKeeper", "PushButton", nullptr));
    } // retranslateUi

};

namespace Ui {
    class NotesKeeper: public Ui_NotesKeeper {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FORM_H
