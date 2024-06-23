# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(614, 429)
        self.centralwidget = QWidget(Camera)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_category = QLabel(self.centralwidget)
        self.label_category.setObjectName(u"label_category")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_category.sizePolicy().hasHeightForWidth())
        self.label_category.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_category.setFont(font)

        self.verticalLayout.addWidget(self.label_category)

        self.viewfinder = QVideoWidget(self.centralwidget)
        self.viewfinder.setObjectName(u"viewfinder")

        self.verticalLayout.addWidget(self.viewfinder)

        Camera.setCentralWidget(self.centralwidget)

        self.retranslateUi(Camera)

        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Camera", None))
        self.label_category.setText(QCoreApplication.translate("Camera", u"Gesto:", None))
    # retranslateUi

