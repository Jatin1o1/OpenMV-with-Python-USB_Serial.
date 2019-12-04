import sys, serial, struct
port = 'COM9'
sp = serial.Serial(port, baudrate=115200)
#sp.setDTR(True) # dsrdtr is ignored on Windows.
#sp.flush()
print("starting")
while 1:
    #print("in while loop")
    b= sp.read().decode('utf-8')
    print(b)
