from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from google.protobuf.json_format import ParseDict


def parseInt(text: str):
    if text.startswith('0x'):
        return int(text, 16)
    elif text == '':
        return 0
    elif '.' in text:
        return float(text)
    else:
        return int(text)


def create_set_function(self, obj, *args, **kwargs):
    def function_template(*args, **kwargs):
        tmp = {}
        for item in obj.horizontalLayouts:
            if isinstance(item, MsgNameQHBoxLayout):
                mgs_name = item.Label.text()
                tmp[mgs_name] = {}
            elif isinstance(item, SetQHBoxLayout):
                name = item.Label.text()
                value = parseInt(item.lineEdit.text())
                if name in self.proto_dict.keys():
                    tmp[name] = [value]
                else:
                    tmp[mgs_name][name] = value
        ParseDict(tmp, self.app)

    return function_template


class SetQHBoxLayout(QHBoxLayout):
    def __init__(self, scrollAreaWidgetContents, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

        self.Label = QLabel(scrollAreaWidgetContents)
        self.Label.setFixedSize(QSize(100, 20))
        self.Label.setText(self.name)
        self.addWidget(self.Label)
        self.lineEdit = QLineEdit(scrollAreaWidgetContents)
        self.lineEdit.setFixedSize(QSize(80, 20))
        self.addWidget(self.lineEdit)


class MsgNameQHBoxLayout(QHBoxLayout):
    def __init__(self, scrollAreaWidgetContents, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

        self.Label = QLabel(scrollAreaWidgetContents)
        self.Label.setFixedSize(QSize(100, 20))
        self.Label.setText(self.name)
        self.addWidget(self.Label)


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

        self.pushButtonS = QPushButton(centralWidget)
        self.pushButtonS.setFixedSize(QSize(40, 20))
        self.pushButtonS.setText("Set")
        self.verticalLayout_m.addWidget(self.pushButtonS)

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
            if isinstance(val, int):
                tmp = SetQHBoxLayout(self.scrollAreaWidgetContents, key)
                self.horizontalLayouts.append(tmp)
            elif isinstance(val, dict):
                label_ = MsgNameQHBoxLayout(self.scrollAreaWidgetContents, key)
                self.horizontalLayouts.append(label_)
                for x, y in val.items():
                    tmp = SetQHBoxLayout(self.scrollAreaWidgetContents, x)
                    self.horizontalLayouts.append(tmp)

        for x in self.horizontalLayouts:
            self.verticalLayout.addLayout(x)

        self.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_m.addWidget(self)

