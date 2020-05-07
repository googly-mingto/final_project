import BT
import maze
import score

# hint: You may design additional functions to execute the input command, which will be helpful when debugging :)

class interface:
    def __init__(self):
        print("")
        print("Arduino Bluetooth Connect Program.")
        print("")
        self.ser = BT.bluetooth()
        port = input("PC bluetooth port name: ")
        while(not self.ser.do_connect(port)):
            if(port == "quit"):
                self.ser.disconnect()
                quit()
            port = input("PC bluetooth port name: ")
        input("Press enter to start.")
        self.ser.SerialWrite('s')

    def get_UID(self):
        return self.ser.SerialReadByte()

    def save_action(self,dirc):
        # TODO : send the action to car
        if dirc == 1:
            message = 'a'
        elif dirc == 2:
            message = 'u'
        elif dirc == 3:
            message = 'r'
        elif dirc == 4:
            message = 'l'
        elif dirc == 5:
            message = 'h'

        return message

    def send_action(self,dirc_m):
        # TODO : send the action to car
        print('action:' + dirc_m)
        return self.ser.SerialWrite(dirc_m)

    def get_message(self):
        return self.ser.SerialReadString()


    def end_process(self):
        self.ser.SerialWrite('e')
        self.ser.disconnect()

if __name__ == '__main__':
    interf = interface()
    