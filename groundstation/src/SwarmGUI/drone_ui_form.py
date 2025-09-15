# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dronenode.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(450, 450)
        GroupBox.setStyleSheet(u"font: 13pt \"Arial\";color:rgb(22, 255, 0);border: 1px solid white;")
        self.gridLayoutWidget = QWidget(GroupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 30, 441, 311))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget.setStyleSheet("background-color: transparent;")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 13pt \"Arial\";color:(0, 255, 2)")
        self.label.setPixmap(QPixmap(u"pixel_quadcopter_top_left_100.png"))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 5, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(3, 255, 21)")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 5, 1, 1, 1)


        self.retranslateUi(GroupBox)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        GroupBox.setTitle(QCoreApplication.translate("GroupBox", u"Drone", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("GroupBox", u"Flightmode", None))
        self.label_3.setText(QCoreApplication.translate("GroupBox", u"Battery status", None))
        self.label_6.setText(QCoreApplication.translate("GroupBox", u"Connected ", None))
        self.pushButton_2.setText(QCoreApplication.translate("GroupBox", u"Land", None))
        self.pushButton_3.setText(QCoreApplication.translate("GroupBox", u"Takeoff", None))
        self.pushButton.setText(QCoreApplication.translate("GroupBox", u"Start search", None))
        self.label_4.setText(QCoreApplication.translate("GroupBox", u"<html><head/><body><p>GPS status</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("GroupBox", u"Altitude", None))
        self.radioButton.setText(QCoreApplication.translate("GroupBox", u"Search alg 1", None))
        self.radioButton_3.setText(QCoreApplication.translate("GroupBox", u"Search alg 2", None))
        self.radioButton_2.setText(QCoreApplication.translate("GroupBox", u"Search alg 3", None))
    # retranslateUi

