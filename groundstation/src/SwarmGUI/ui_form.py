# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_SwarmCommanderGUI(object):
    def setupUi(self, SwarmCommanderGUI):
        if not SwarmCommanderGUI.objectName():
            SwarmCommanderGUI.setObjectName(u"SwarmCommanderGUI")
        SwarmCommanderGUI.resize(800, 600)
        SwarmCommanderGUI.setStyleSheet(u"background-color: \"black\";")
        self.actionEdit_Geofence = QAction(SwarmCommanderGUI)
        self.actionEdit_Geofence.setObjectName(u"actionEdit_Geofence")
        self.actionSet_geofence = QAction(SwarmCommanderGUI)
        self.actionSet_geofence.setObjectName(u"actionSet_geofence")
        self.actionReset_geofence = QAction(SwarmCommanderGUI)
        self.actionReset_geofence.setObjectName(u"actionReset_geofence")
        self.actionAdd_agent = QAction(SwarmCommanderGUI)
        self.actionAdd_agent.setObjectName(u"actionAdd_agent")
        self.actionRemove_agent = QAction(SwarmCommanderGUI)
        self.actionRemove_agent.setObjectName(u"actionRemove_agent")
        self.centralwidget = QWidget(SwarmCommanderGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 260, 58, 16))
        SwarmCommanderGUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SwarmCommanderGUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menubar.setStyleSheet(u"font: 13pt \"Arial\";color: rgb(1, 255, 23);")
        self.menuAgents = QMenu(self.menubar)
        self.menuAgents.setObjectName(u"menuAgents")
        self.menuGeofence = QMenu(self.menubar)
        self.menuGeofence.setObjectName(u"menuGeofence")
        SwarmCommanderGUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SwarmCommanderGUI)
        self.statusbar.setObjectName(u"statusbar")
        SwarmCommanderGUI.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAgents.menuAction())
        self.menubar.addAction(self.menuGeofence.menuAction())
        self.menuAgents.addAction(self.actionAdd_agent)
        self.menuAgents.addAction(self.actionRemove_agent)
        self.menuGeofence.addAction(self.actionEdit_Geofence)
        self.menuGeofence.addAction(self.actionSet_geofence)
        self.menuGeofence.addAction(self.actionReset_geofence)

        self.retranslateUi(SwarmCommanderGUI)

        QMetaObject.connectSlotsByName(SwarmCommanderGUI)
    # setupUi

    def retranslateUi(self, SwarmCommanderGUI):
        SwarmCommanderGUI.setWindowTitle(QCoreApplication.translate("SwarmCommanderGUI", u"SwarmCommanderGUI", None))
        self.actionEdit_Geofence.setText(QCoreApplication.translate("SwarmCommanderGUI", u"Edit geofence", None))
        self.actionSet_geofence.setText(QCoreApplication.translate("SwarmCommanderGUI", u"Set geofence", None))
        self.actionReset_geofence.setText(QCoreApplication.translate("SwarmCommanderGUI", u"Reset geofence", None))
        self.actionAdd_agent.setText(QCoreApplication.translate("SwarmCommanderGUI", u"Add agent", None))
        self.actionRemove_agent.setText(QCoreApplication.translate("SwarmCommanderGUI", u"Remove agent", None))
        self.label.setText(QCoreApplication.translate("SwarmCommanderGUI", u"testtting", None))
        self.menuAgents.setTitle(QCoreApplication.translate("SwarmCommanderGUI", u"Agents", None))
        self.menuGeofence.setTitle(QCoreApplication.translate("SwarmCommanderGUI", u"Geofence", None))
    # retranslateUi

