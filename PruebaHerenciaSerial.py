import serial



class ModemUSB(serial.Serial):

    def tipo_serial(self):
        return "ModemUSB"
    
    def scan(self):
        available = []
        for i in range(256):
            try:
                self.port = i
                self.open()
                available.append( (i, self.portstr))
                self.close()
            except serial.SerialException:
                pass
        return available





if __name__=='__main__':

    Port = ModemUSB()
    print Port.tipo_serial()

    ports_habil = Port.scan()

    print "Found ports:"
    for n,s in ports_habil:
        print "(%d) %s" % (n,s)

    
