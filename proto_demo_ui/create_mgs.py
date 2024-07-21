
import serial

from generation.py_gen import proto_app_pb2


class MsgManager:
    def __init__(self):
        self.dev = serial.Serial('/tmp/ttyV0', baudrate=115200)

    def send(self, msg):
        data = msg.SerializeToString()
        self.dev.write(data)

    def read(self):
        app = proto_app_pb2.Application()
        tmp = self.dev.readall()
        app.ParseFromString(tmp)
        return app
