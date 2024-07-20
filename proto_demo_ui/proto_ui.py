
from loguru import logger

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from proto_demo_ui.qtareas.proto_info import ProtoInfoScrollArea
from proto_demo_ui.qtareas.proto_set import ProtoSetScrollArea


class MainWindow(QMainWindow):
    def __init__(self, proto_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proto_dict = proto_dict
        self.setupUi()
        self._init_buttons()

    def closeEvent(self, event):
        logger.info(f'closed')

    def _init_buttons(self):
        logger.info(f'_init_buttons')

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
        for key, val in self.proto_dict.items():
            if isinstance(val, dict):
                self.area_list.append(
                    ProtoSetScrollArea(
                        self.centralWidget,
                        f"set_{key}",
                        val,
                    )
                )
            else:
                self.area_list.append(
                    ProtoSetScrollArea(
                        self.centralWidget,
                        f"set_{key}",
                        {key: val},
                    )
                )

        self.area_list.append(
            ProtoInfoScrollArea(
            self.centralWidget,
            "proto_support",
                None,
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
