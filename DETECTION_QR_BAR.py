#WE USE PYZBAR FOR QR READING
import cv2
import numpy as np
from pyzbar.pyzbar import decode


'''decode is the function we are going to use'''
#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):                #if the image has more then one barcodes
        #print(barcode.data)       #print out the data of the barcode        #b means in byte
        myData = barcode.data.decode('utf-8')          #byte to string
        print(myData)                #string now
        #print(barcode.rect)       #print out the boundary box of the barcode


        #BOUNDING BOX-use polygon -- we have to convert it into an array and  reshape array and send it to polygon lines function(FORMALITY SO HAVE TO DO IT)
        #If we used rectange, it wont work if we rotate the image, which is not good
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)            #image,points,closed?,color,thickness
        pts2 = barcode.rect
        # to put text over image..   image, data to put, we are using pts so that the text wont rotate when we rotate the image,font,size,color,thickness
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)


    cv2.imshow('RESULT', img)
    cv2.waitKey(1)