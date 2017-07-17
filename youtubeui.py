#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created: Mon Jun  5 16:25:53 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from parse import *
from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def setupUi(self, Dialog):



        Dialog.setObjectName(_fromUtf8("yboxplayer"))
        Dialog.resize(731, 300)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 711, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 80, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 711, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.search)
	self.listWidget.itemClicked.connect(self.copy)
        self.listWidget.itemDoubleClicked.connect(self.surf)

    def search(self):
        # this function is for searching into the youtube
        import subprocess
        keyword = str(unicode(self.lineEdit.text()))
        subprocess.call(["python", "search.py", "--q", keyword])
        video_list = []
        self.listWidget.clear()
        video_ret = parse_vid(video_list)
        #print video_ret
        # print len(video_list)
        self.listWidget.addItems(video_ret)

#######################################################################
    def copy(self):
        url = parse_url(self.listWidget.currentRow())
        import subprocess
        URL = "https://www.youtube.com/watch?v=" + url
	clipboard = QtGui.QApplication.clipboard()
	clipboard.setText(URL)        


#######################################################################
    def surf(self):
        url = parse_url(self.listWidget.currentRow())
        import subprocess
        URL = "https://www.youtube.com/watch?v=" + url
        subprocess.call(["mpv", URL])


########################################################################
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Youboxplayer", None))
        Dialog.setWindowIcon(QtGui.QIcon('yboxplayer.png'))
        self.pushButton.setText(_translate("Dialog", "Search", None))
        self.label.setText(_translate("Dialog", "Search Result", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

