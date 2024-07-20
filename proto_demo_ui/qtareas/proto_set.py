from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class SetQHBoxLayout(QHBoxLayout):
    def __init__(self, scrollAreaWidgetContents, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

        self.Label = QLabel(scrollAreaWidgetContents)
        self.Label.setFixedSize(QSize(100, 20))
        self.Label.setText(self.name)
        self.addWidget(self.Label)
        self.pushButtonS = QPushButton(scrollAreaWidgetContents)
        self.pushButtonS.setFixedSize(QSize(40, 20))
        self.pushButtonS.setText("Set")
        self.addWidget(self.pushButtonS)
        self.lineEdit = QLineEdit(scrollAreaWidgetContents)
        self.lineEdit.setFixedSize(QSize(80, 20))
        self.addWidget(self.lineEdit)


class ProtoSetScrollArea(QScrollArea):
    def __init__(self, centralWidget, name, proto_dict, *args, **kwargs):
        super().__init__(centralWidget, *args, **kwargs)
        self.name = name
        self.proto_dict = proto_dict
        self.deser = None

        self.verticalLayout_m = QVBoxLayout()
        self.verticalLayout_m.setObjectName(u"verticalLayout")
        self.label_ = QLabel(centralWidget)
        self.label_.setObjectName(u"label_")
        self.label_.setText(self.name)
        self.verticalLayout_m.addWidget(self.label_)

        self.repeat_get = QCheckBox(centralWidget)
        self.repeat_get.setText('get repeat 2s')
        self.verticalLayout_m.addWidget(self.repeat_get)

        self.setGeometry(QRect(10, 10, 400, 300))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 400, 300))

        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayouts = []
        for key, val in self.proto_dict.items():
            tmp = SetQHBoxLayout(self.scrollAreaWidgetContents, key)
            self.horizontalLayouts.append(tmp)
        for x in self.horizontalLayouts:
            self.verticalLayout.addLayout(x)

        self.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_m.addWidget(self)

    def checkbox_update(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label2)
        if self.repeat_get.isChecked():
            self.timer.start(2000)
        else:
            self.timer.stop()
