
import serial

from generation.py_gen import proto_app_pb2


class MsgManager:
    def __init__(self, port, baudrate):
        self.dev = serial.Serial(port, baudrate=baudrate, timeout=1)

    def send(self, msg):
        data = msg.SerializeToString()
        self.dev.write(data)

    def read(self):
        app = proto_app_pb2.Application()
        tmp = self.dev.readall()
        app.ParseFromString(tmp)
        return app
