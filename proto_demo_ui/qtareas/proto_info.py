
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class ProtoInfoScrollArea(QScrollArea):
    def __init__(self, centralWidget, name, deser, *args, **kwargs):
        super().__init__(centralWidget, *args, **kwargs)
        self.name = name
        self.deser = deser

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

        self.label2 = QLabel(self.scrollAreaWidgetContents)
        self.label2.setText("datas")
        self.verticalLayout.addWidget(self.label2)



        self.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_m.addWidget(self)

    def checkbox_update(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label2)
        if self.repeat_get.isChecked():
            self.timer.start(2000)
        else:
            self.timer.stop()

    def update_label2(self):
        tmp_str = f"status:\n{self.deser.get_debug_status()}\n"
        tmp_str += f"info:\n{self.deser.get_debug_info()}\n"
        self.label2.setText(f'{tmp_str}')
