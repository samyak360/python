#!/usr/bin/python3

import cv2
import numpy as np
#loading face xml database
face_cascade = cv2.CascadeClassifier('face.xml')
#starting webcam
cap = cv2.VideoCapture(0)

# capture 3 consecutive frames
take_frame1=cap.read()[1]
take_frame2=cap.read()[1]
take_frame3=cap.read()[1]

#  converting all 3 frames to grayscale
gray_img1=cv2.cvtColor(take_frame1,cv2.COLOR_BGR2GRAY)
gray_img2=cv2.cvtColor(take_frame2,cv2.COLOR_BGR2GRAY)
gray_img3=cv2.cvtColor(take_frame3,cv2.COLOR_BGR2GRAY)

#  creating function for making image as abs diff
def  myimg_diff(x,y,z):
	diff1=cv2.absdiff(x,y)
	diff2=cv2.absdiff(y,z)
	final_diff=cv2.bitwise_and(diff1,diff2)
	return final_diff


while(cap.isOpened()):
	#reading camera frame
	status,img=cap.read()
	#converting color image into grayscale image
	grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#trying multi angle in grayscaled img       #tunning parameter
	faces=face_cascade.detectMultiScale(grayimg,1.15,5)
	
	#applying iteration in multi scaled variable
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]

	#detection of moving object
	diff_imgdata=myimg_diff(gray_img1,gray_img2,gray_img3)
	# replacing frames 
	gray_img1=gray_img2
	gray_img2=gray_img3
	gray_img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	if(faces==() ):
		print("")
	elif (faces!=()):
		print("face is found")

	cv2.imshow('imgw',img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()


	
