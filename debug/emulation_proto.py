
import time
import serial
from loguru import logger
from generation.py_gen import proto_app_pb2


def main():

    dev_rs = serial.Serial(port='/tmp/ttyV1', baudrate=115200, timeout=1)

    while True:
        tmp = dev_rs.readall()
        app = proto_app_pb2.Application()
        app.ParseFromString(tmp)
        logger.info(f'vals {app=}')
        dev_rs.write(app.SerializeToString())


if __name__ == '__main__':
    main()
