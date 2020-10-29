from cv2 import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
import ctypes
import time
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success, frame = cap.read()
    dec = decode(frame)
    for barcode in dec:
        myData = barcode.data.decode('utf-8')
        if((barcode.type == "QRCODE") ):
            result = ctypes.windll.user32.MessageBoxW(0, "Do you want to open "+ myData, "QRCODE", 4)
            if (result == 6):
                webbrowser.open(myData)
            else:
                time.sleep(1)    
        else:
            ctypes.windll.user32.MessageBoxW(0, "Barcode: "+ myData, "BARCODE", 0)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  
cap.release()
cv2.destroyAllWindows()

