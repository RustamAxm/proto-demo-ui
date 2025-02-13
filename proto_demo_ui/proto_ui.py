
from loguru import logger

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from proto_demo_ui.create_mgs import MsgManager
from proto_demo_ui.qtareas.proto_info import ProtoInfoScrollArea, create_info_function
from proto_demo_ui.qtareas.proto_set import ProtoSetScrollArea, create_set_function
from generation.py_gen import proto_app_pb2


class MainWindow(QMainWindow):
    def __init__(self, proto_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proto_dict = proto_dict
        self.app_out = proto_app_pb2.Application()
        self.app_in = proto_app_pb2.Application()
        self.msg_manager = MsgManager('/tmp/ttyV0', 115200)
        self.setupUi()
        self._init_buttons()

    def closeEvent(self, event):
        logger.info(f'closed')

    def _init_buttons(self):
        logger.info(f'_init_buttons')
        for area in self.area_list:
            if isinstance(area, ProtoSetScrollArea):
                fnc = create_set_function(self, area)
                area.pushButtonS.clicked.connect(fnc)
            elif isinstance(area, ProtoInfoScrollArea):
                area.repeat_get.clicked.connect(area.checkbox_update)

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")

        x_size = 400
        y_size = 800
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName(u"centralWidget")

        self.horizontalLayout_main = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.horizontalLayout_main.setContentsMargins(10, 10, 10, 10)

        self.area_list = []
        self.area_list.append(
            ProtoSetScrollArea(
                self.centralWidget,
                f"set_",
                self.proto_dict,
            )
        )

        self.area_list.append(
            ProtoInfoScrollArea(
            self.centralWidget,
            "proto_support",
                self.msg_manager,
            )
        )

        for i, x in enumerate(self.area_list):
            self.horizontalLayout_main.addLayout(x.verticalLayout_m)

        self.setCentralWidget(self.centralWidget)
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        self.resize(x_size, y_size)

    def retranslateUi(self):
        self.setWindowTitle(f"proto tester")
