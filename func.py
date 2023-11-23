# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'func.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 300)
        Dialog.setMinimumSize(QtCore.QSize(420, 300))
        Dialog.setMaximumSize(QtCore.QSize(420, 300))
        Dialog.setStyleSheet("QDialog{\n"
                             "background-color: rgb(4, 1, 31);\n"
                             "border-bottom-right-radius: 9px;\n"
                             "border-bottom-left-radius: 9px;\n"
                             "}")
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(160, 260, 113, 32))
        self.OK.setObjectName("OK")
        self.Sintaxis = QtWidgets.QTextEdit(Dialog)
        self.Sintaxis.setGeometry(QtCore.QRect(23, 80, 381, 175))
        self.Sintaxis.setStyleSheet("QTextEdit{\n"
                                    "background-color: rgb(4, 1, 31);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar:vertical {              \n"
                                    " background:rgb(4, 1, 31);\n"
                                    " width:10px;\n"
                                    " margin: 0px 0px 0px 0px;\n"
                                    " border-radius: 5.4px\n"
                                    "}\n"
                                    "QScrollBar::handle:vertical {\n"
                                    " background: rgba(131, 131, 131, 180);\n"
                                    " min-height: 0px;\n"
                                    " border-radius: 4px\n"
                                    "}\n"
                                    "QScrollBar::add-line:vertical {\n"
                                    " background: rgb(4, 1, 31);\n"
                                    " height: 0px;\n"
                                    " ubcontrol-position: bottom;\n"
                                    " subcontrol-origin: margin;\n"
                                    "}\n"
                                    "QScrollBar::sub-line:vertical {\n"
                                    " background: rgb(4, 1, 31);\n"
                                    " height: 0 px;\n"
                                    " subcontrol-position: top;\n"
                                    " subcontrol-origin: margin;\n"
                                    "}")
        self.Sintaxis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Sintaxis.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Sintaxis.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Sintaxis.setReadOnly(True)
        self.Sintaxis.setObjectName("Sintaxis")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(18, 4, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DifCuad = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DifCuad.setMinimumSize(QtCore.QSize(165, 22))
        self.DifCuad.setMaximumSize(QtCore.QSize(165, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.DifCuad.setFont(font)
        self.DifCuad.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(32, 132, 255);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: rgb(240, 240, 240);\n"
                                   "    color: rgb(251, 251, 251);\n"
                                   "    border-style: inset;\n"
                                   "}")
        self.DifCuad.setCheckable(False)
        self.DifCuad.setChecked(False)
        self.DifCuad.setAutoRepeat(False)
        self.DifCuad.setAutoExclusive(False)
        self.DifCuad.setObjectName("DifCuad")
        self.horizontalLayout.addWidget(self.DifCuad)
        self.Tri = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Tri.setMinimumSize(QtCore.QSize(80, 22))
        self.Tri.setMaximumSize(QtCore.QSize(80, 22))
        self.Tri.setStyleSheet("QPushButton {\n"
                               "    background-color: white;\n"
                               "    color: rgb(0, 0, 0);\n"
                               "    border-radius: 5px;\n"
                               "}\n"
                               "QPushButton:pressed {\n"
                               "    background-color: rgb(240, 240, 240);\n"
                               "    color: rgb(251, 251, 251);\n"
                               "    border-style: inset;\n"
                               "}")
        self.Tri.setObjectName("Tri")
        self.horizontalLayout.addWidget(self.Tri)
        self.FC = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.FC.setMinimumSize(QtCore.QSize(100, 22))
        self.FC.setMaximumSize(QtCore.QSize(100, 22))
        self.FC.setStyleSheet("QPushButton {\n"
                              "    background-color: white;\n"
                              "    color: rgb(0, 0, 0);\n"
                              "    border-radius: 5px;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "    background-color: rgb(240, 240, 240);\n"
                              "    color: rgb(251, 251, 251);\n"
                              "    border-style: inset;\n"
                              "}")
        self.FC.setObjectName("FC")
        self.horizontalLayout.addWidget(self.FC)
        self.exp = QtWidgets.QTextEdit(Dialog)
        self.exp.setGeometry(QtCore.QRect(90, 46, 211, 28))
        self.exp.setStyleSheet("QTextEdit{\n"
                               "background-color: rgb(4, 1, 31);\n"
                               "color: rgb(255, 255, 255);\n"
                               "}\n"
                               "\n"
                               "QScrollBar:vertical {              \n"
                               " background:rgb(4, 1, 31);\n"
                               " width:10px;\n"
                               " margin: 0px 0px 0px 0px;\n"
                               " border-radius: 5.4px\n"
                               "}\n"
                               "QScrollBar::handle:vertical {\n"
                               " background: rgba(131, 131, 131, 180);\n"
                               " min-height: 0px;\n"
                               " border-radius: 4px\n"
                               "}\n"
                               "QScrollBar::add-line:vertical {\n"
                               " background: rgb(4, 1, 31);\n"
                               " height: 0px;\n"
                               " ubcontrol-position: bottom;\n"
                               " subcontrol-origin: margin;\n"
                               "}\n"
                               "QScrollBar::sub-line:vertical {\n"
                               " background: rgb(4, 1, 31);\n"
                               " height: 0 px;\n"
                               " subcontrol-position: top;\n"
                               " subcontrol-origin: margin;\n"
                               "}")
        self.exp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.exp.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.exp.setReadOnly(True)
        self.exp.setObjectName("exp")
        self.exp.setMinimumWidth(250)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.DifCuad.clicked.connect(self.dc_clicked)
        self.Tri.clicked.connect(self.tri_clicked)
        self.FC.clicked.connect(self.fc_clicked)

        self.Dialog = Dialog
        self.OK.clicked.connect(self.ok_clicked)

    def ok_clicked(self):
        self.Dialog.close()

    def dc_clicked(self):
        self.DifCuad.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(32, 132, 255);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: rgb(240, 240, 240);\n"
                                   "    color: rgb(251, 251, 251);\n"
                                   "    border-style: inset;\n"
                                   "}")

        self.Tri.setStyleSheet("QPushButton {\n"
                              "    background-color: white;\n"
                              "    color: rgb(0, 0, 0);\n"
                              "    border-radius: 5px;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "    background-color: rgb(240, 240, 240);\n"
                              "    color: rgb(251, 251, 251);\n"
                              "    border-style: inset;\n"
                              "}")
        self.FC.setStyleSheet("QPushButton {\n"
                              "    background-color: white;\n"
                              "    color: rgb(0, 0, 0);\n"
                              "    border-radius: 5px;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "    background-color: rgb(240, 240, 240);\n"
                              "    color: rgb(251, 251, 251);\n"
                              "    border-style: inset;\n"
                              "}")

        self.Sintaxis.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Sintaxis</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Para <span style=\" font-weight:600; font-style:italic;\">a</span> (Primer término) y <span style=\" font-weight:600; font-style:italic;\">b</span> (Segundo término) ingresar: </p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> - Coeficiente</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> - Variables junto con sus exponentes</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">En la forma:</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">CoeficienteVariable**(exponente)</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#f75057;\">Nota:</span> No es necesario colocar el signo de <span style=\" font-weight:600; font-style:italic;\">b</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Ejemplo</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9x<span style=\" vertical-align:super;\">2 </span>- 16</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el primer término ingresar: 9x**(2)</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el segundo término ingresar: 16</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.exp.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a<span style=\" vertical-align:super;\">2</span> - b<span style=\" vertical-align:super;\">2</span> = (a - b)(a + b)</p></body></html>")

    def tri_clicked(self):
        self.Tri.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(32, 132, 255);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: rgb(240, 240, 240);\n"
                                   "    color: rgb(251, 251, 251);\n"
                                   "    border-style: inset;\n"
                                   "}")

        self.DifCuad.setStyleSheet("QPushButton {\n"
                               "    background-color: white;\n"
                               "    color: rgb(0, 0, 0);\n"
                               "    border-radius: 5px;\n"
                               "}\n"
                               "QPushButton:pressed {\n"
                               "    background-color: rgb(240, 240, 240);\n"
                               "    color: rgb(251, 251, 251);\n"
                               "    border-style: inset;\n"
                               "}")
        self.FC.setStyleSheet("QPushButton {\n"
                              "    background-color: white;\n"
                              "    color: rgb(0, 0, 0);\n"
                              "    border-radius: 5px;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "    background-color: rgb(240, 240, 240);\n"
                              "    color: rgb(251, 251, 251);\n"
                              "    border-style: inset;\n"
                              "}")

        self.Sintaxis.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Sintaxis</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Para <span style=\" font-weight:600; font-style:italic;\">a</span> (Primer término) y <span style=\" font-weight:600; font-style:italic;\">b</span> (Segundo término) ingresar solamente el coeficiente del término, y en <span style=\" font-weight:600; font-style:italic;\">c</span> (Tercer término) la constante, todos con sus respectivos signos. </p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Los términos están ordenados de manera descendente según los grados de <span style=\" font-style:italic;\">x</span>:</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- La variable del primer término es x<span style=\" vertical-align:super;\">2</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- La variable del tercer término es x</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- El tercer término no prersenta variable (x<span style=\" vertical-align:super;\">0</span>), por lo que <span style=\" font-weight:600; font-style:italic;\">c</span> es una constante</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Ejemplo</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18x<span style=\" vertical-align:super;\">2 </span>- 13 - 5</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el primer término ingresar: 18</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el segundo término ingresar: -13</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el tercer término ingresar: -5</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.exp.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ax<span style=\" vertical-align:super;\">2</span> + bx +c =&gt; a<span style=\" vertical-align:super;\">2 </span>+ 2ab + b<span style=\" vertical-align:super;\">2</span> = (a+b)<span style=\" vertical-align:super;\">2</span></p></body></html>")

    def fc_clicked(self):
        self.FC.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(32, 132, 255);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: rgb(240, 240, 240);\n"
                                   "    color: rgb(251, 251, 251);\n"
                                   "    border-style: inset;\n"
                                   "}")

        self.DifCuad.setStyleSheet("QPushButton {\n"
                               "    background-color: white;\n"
                               "    color: rgb(0, 0, 0);\n"
                               "    border-radius: 5px;\n"
                               "}\n"
                               "QPushButton:pressed {\n"
                               "    background-color: rgb(240, 240, 240);\n"
                               "    color: rgb(251, 251, 251);\n"
                               "    border-style: inset;\n"
                               "}")
        self.Tri.setStyleSheet("QPushButton {\n"
                              "    background-color: white;\n"
                              "    color: rgb(0, 0, 0);\n"
                              "    border-radius: 5px;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "    background-color: rgb(240, 240, 240);\n"
                              "    color: rgb(251, 251, 251);\n"
                              "    border-style: inset;\n"
                              "}")

        self.Sintaxis.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                              "p, li { white-space: pre-wrap; }\n"
                              "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Sintaxis</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dependiendo del grado elegido, la expresión podrá tener hasta 6 términos. El principio de la sintaxis es el mismo que el de los trinomios: Solamente se ingresa los coeficientes y la constante (todos con sus respectivos signos) en orden descendente según los grados de <span style=\" font-style:italic;\">x</span>. </p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Ejemplo</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4x<span style=\" vertical-align:super;\">4</span> - 6x<span style=\" vertical-align:super;\">3</span> - 2x<span style=\" vertical-align:super;\">2</span> + 12x</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el primer término ingresar: 4</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el segundo término ingresar: -6</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el tercer término ingresar: -2</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el cuarto término ingresar: 5</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el quinto término ingresar: 0 (Ya que la constante no tiene un valor en esta expresión)</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.exp.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                         "p, li { white-space: pre-wrap; }\n"
                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a<span style=\" vertical-align:super;\">2</span> - b<span style=\" vertical-align:super;\">2</span> = (a - b)(a + b)</p></body></html>")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OK.setText(_translate("Dialog", "OK"))
        self.Sintaxis.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Sintaxis</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Para <span style=\" font-weight:600; font-style:italic;\">a</span> (Primer término) y <span style=\" font-weight:600; font-style:italic;\">b</span> (Segundo término) ingresar: </p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> - Coeficiente</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> - Variables junto con sus exponentes</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">En la forma:</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">CoeficienteVariable**(exponente)</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#f75057;\">Nota:</span> No es necesario colocar el signo de <span style=\" font-weight:600; font-style:italic;\">b</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Ejemplo</span></p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9x<span style=\" vertical-align:super;\">2 </span>- 16</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el primer término ingresar: 9x**(2)</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- En el segundo termino ingresar: 16</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.DifCuad.setText(_translate("Dialog", "Diferencia de Cuadrados"))
        self.Tri.setText(_translate("Dialog", "Trinomios"))
        self.FC.setText(_translate("Dialog", "Factor común"))
        self.exp.setHtml(_translate("Dialog",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a<span style=\" vertical-align:super;\">2</span> - b<span style=\" vertical-align:super;\">2</span> = (a - b)(a + b)</p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())