from pyb import USB_VCP   # importing the library for USb VCP(Virtual Comm Port).
usb = USB_VCP()   # makes USB object

while(True):                # making a loop to continously send data
    usb.send("hi123")       # send function to send script.




'''  NOTE
 usb.send() fucntion send the data character by character.
 for ex: usb.send("hi123") send the "hi123" string as "h", "i", "1", "2", "3".
'''

