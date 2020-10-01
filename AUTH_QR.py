#WE USE PYZBAR FOR QR READING
import cv2
import numpy as np
from pyzbar.pyzbar import decode
########################################################################################
#change log -
# 1)fixed polygon bug         * 8-7-2020 12:32pm *
# 2)can work on more then 1 codes.   * 22-7-2020 9:13pm *
# 3)accuracy increased in case of webcam.  * 10-8-2020 4:04pm *
# 4)colors added.   * 11-8-2020 2:24pm *

########################################################################################

'''decode is the function we are going to use'''
#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('myTextData') as f:
    myTextData = f.read().splitlines()
#print(myTextData)


while True:
    success, img = cap.read()
    #success=cap.grab()
    for barcode in decode(img):                #if the image has more then one barcodes
        #print(barcode.data)       #print out the data of the barcode        #b means in byte
        myData = barcode.data.decode('utf-8')          #byte to string
        print(myData)                #string now

        if myData in myTextData:
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            myOutput = 'UnAuthorized'
            myColor = (0,0,255)
        #print(barcode.rect)       #print out the boundary box of the barcode


        #BOUNDING BOX-use polygon -- we have to convert it into an array and  reshape array and send it to polygon lines function(FORMALITY SO HAVE TO DO IT)
        #If we used rectange, it wont work if we rotate the image, which is not good
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)            #image,points,closed?,color,thickness
        pts2 = barcode.rect
        # to put text over image..   image, data to put, we are using pts so that the text wont rotate when we rotate the image,font,size,color,thickness
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)


    cv2.imshow('RESULT', img)
    cv2.waitKey(1)


##################################################
# ---------------to do-------------
# 1)hide the original code in runtime terminal
# 2)increase distance accuracy.
