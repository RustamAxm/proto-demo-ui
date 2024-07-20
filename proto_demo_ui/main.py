import sys

from PySide2.QtWidgets import QApplication

from proto_demo_ui.proto_test import get_proto_dict
from proto_demo_ui.proto_ui import MainWindow


def main():
    proto_dict = get_proto_dict()
    app = QApplication(sys.argv)
    window = MainWindow(proto_dict)

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
