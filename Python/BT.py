from time import sleep
import serial
# these codes are for bluetooth
# hint: please check the function "sleep". how does it work?

class bluetooth:
    def __init__(self):
        self.ser = serial.Serial()

    def do_connect(self,port):
        self.ser.close()
        print("Connecting...")
        try:
            self.ser = serial.Serial(port,9600,timeout=2)
            print("connect success")
            print("")
        except serial.serialutil.SerialException:
            print("fail to connect")
            print("")
            return False
        return True


    def disconnect(self):
        self.ser.close()

    def SerialWrite(self,output):
        # send = 's'.encode("utf-8")
        send = output.encode("utf-8")
        self.ser.write(send)

    def SerialReadString(self):
        # TODO: Get the information from Bluetooth. Notice that the return type should be transformed into hex.
        sleep(0.05)
        waiting = self.ser.in_waiting
        if waiting :
            rv = self.ser.read(waiting).decode("utf-8")
            self.ser.flushInput()
            print(rv)
            return rv
        #print('nothing to read')
        return ""

    def SerialReadByte(self):
        sleep(1)
        waiting = self.ser.in_waiting
        
        rv = self.ser.read(waiting)
        if(rv):
            print(waiting)
            print(rv)
            print(int(rv, 16))
            temp = int(rv, 16).to_bytes(4, byteorder='big')
            UID = hex(int.from_bytes(temp, byteorder='big', signed=False))
            self.ser.flushInput()
            return UID
        else:
            return 0
    

