
import serial
port = 'COM9'
sp = serial.Serial(port, baudrate=115200)

print("starting")
str=""
while 1:
    b= sp.read().decode('utf-8')  # decoing the input character from the camera
    
    if b is not "*":        #  condition to check the string termination for character concatenation.
        str += b
    else:                   # condition is terminating character is found then print the string and then rest the sting
        print (str)
        str=""              # reseting the string
        
        
