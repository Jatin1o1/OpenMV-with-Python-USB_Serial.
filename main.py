import sensor
from pyb import USB_VCP
usb = USB_VCP()
while(True):
	usb.send("hi123")
