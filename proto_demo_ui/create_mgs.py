import threading

import serial

from generation.py_gen import proto_app_pb2


class MsgManager:
    def __init__(self, port, baudrate):
        self.dev = serial.Serial(port, baudrate=baudrate, timeout=1)
        self.out_app = proto_app_pb2.Application()
        self._th = threading.Thread(target=self.reader, daemon=True)
        self._th.start()

    def send(self, msg):
        data = msg.SerializeToString()
        self.dev.write(data)

    def read(self):
        return self.out_app

    def reader(self):
        while True:
            tmp = self.dev.readall()
            if len(tmp) > 0:
                self.out_app.ParseFromString(tmp)
