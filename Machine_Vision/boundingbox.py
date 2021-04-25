#!/usr/bin/env python3
import cv2 
image = cv2.imread("bbtestimg.jpg")
#image = cv2.imread("cropped.jpg") 
#new_image = image.copy()

#y=100
#x=440
#h=915
#w=1160

#crop_img = new_image[y:y+h, x:x+w]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)

start_point = (450, 110)	#first value moves the left y axis horizontally, 2nd moves the top x axis vertically
end_point = (1590, 1005)	#first value moves the right y axis horizontally, 2nd moves the bottom x axis verticlally
  
#Blue color in BGR 
color = (255, 0, 0) 
  
#Line thickness of 2 px 
thickness = 2
  
#Using cv2.rectangle() method 
#Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow('original', image)  
cv2.waitKey(0)  #Wait for keypress to continue
cv2.destroyAllWindows()  #Close windows

#cv2.imwrite('boundingbox.jpg', image)

