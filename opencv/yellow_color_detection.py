#!/usr/bin/python3

import cv2
import numpy as np

# start camera
cap=cv2.VideoCapture(0)

while True:

	status,frame=cap.read()
	# capture only red frame
	mask=cv2.inRange(frame,(0,145,170),(50,255,255))
	output=cv2.bitwise_and(frame,frame,mask=mask)
	final_output=np.hstack([frame,output])
	cv2.imshow('yellow_window',final_output)
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()
