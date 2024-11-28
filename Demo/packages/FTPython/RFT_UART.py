import serial
import time
import threading
from RFT_UART_command import *
from RFT_UART_response import *

class RFTseries:
    __response = dict()
    DT = 50
    DF = 1000
    offsetFx, offsetFy, offsetFz, offsetTx, offsetTy, offsetTz = 0, 0, 0, 0, 0, 0
    def __init__(self, port, baud=115200):
        # default 115200 bps
        # 1 stop bit, No parity, No flow control, 8 data bits
        self.ser = serial.Serial(port, baud)
        self.ser.flush()
        self.__thread = threading.Thread(target=self.__readResponseRunner)
        self.__thread.daemon = True
        self.__thread.start()
    def close(self):
        self.ser.close()
    ## Command Packet Structure
    # SOP : 0x55
    # Data Field  : 8 bytes
    # Checksum : 1 byte, summation of data field
    # EOP : 0xAA
    def sendCommand(self, command):
        if len(command) != 8:
            raise ValueError('Data field must be 8 bytes long')
        packet = b'\x55' + command + int.to_bytes(sum(command)) + b'\xAA'
        self.ser.write(packet)
        return packet
    ## Response Packet Structure
    # SOP : 0x55
    # Data Field  : 16 bytes
    # Checksum : 1 byte
    # EOP : 0xAA
    def __readResponseRunner(self):
        while True:
            if self.ser.in_waiting:
                if self.ser.read() == b'\x55':
                    data = self.ser.read(16)
                    checksum = self.ser.read()
                    eop = self.ser.read()
                    responseID = data[0]
                    self.__response[responseID] = data
    def getResponse(self, responseID):
        return self.__response.get(responseID)
    def hardTare(self):
        self.sendCommand(commandSetBias(True))
    def softTare(self):
        self.offsetFx, self.offsetFy, self.offsetFz, self.offsetTx, self.offsetTy, self.offsetTz, _ = responseReadFTData(self.getResponse(ID_START_FT_DATA_OUTPUT))
    def getTareFT(self):
        rawFx, rawFy, rawFz, rawTx, rawTy, rawTz, _ = responseReadFTData(self.getResponse(ID_START_FT_DATA_OUTPUT))
        return rawFx - self.offsetFx, rawFy - self.offsetFy, rawFz - self.offsetFz, rawTx - self.offsetTx, rawTy - self.offsetTy, rawTz - self.offsetTz
