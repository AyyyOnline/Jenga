#!/usr/bin/env python3
import cv2 
image = cv2.imread("eptestimg.jpg") 
new_image = image.copy()

# values for bbtestimg.jpg
#y=100		#higher goes lower down
#x=440		#higher goes right
#h=915		#height of img
#w=1160	#width of img

# values for eptestimg.jpg
y=75		#higher goes lower down
x=385		#higher goes right
h=900		#height of img
w=1150		#width of img

crop_img = new_image[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
cv2.imwrite('cropepimg.jpg', crop_img)

#start_point = (10, 10)	##first value moves the left y axis horizontally, 2nd moves the top x axis vertically
#end_point = (1150, 910)	##first value moves the right y axis horizontally, 2nd moves the bottom x axis verticlally
#  
##Blue color in BGR 
#color = (255, 0, 0) 
#  
##Line thickness of 2 px 
#thickness = 2
  
#Using cv2.rectangle() method 
#Draw a rectangle with blue line borders of thickness of 2 px 
#cropwb = cv2.rectangle(crop_img, start_point, end_point, color, thickness)
#cv2.imshow('cropped with bounding', cropwb)  
#cv2.waitKey(0)  #Wait for keypress to continue
#cv2.destroyAllWindows()  ##Close windows
#cv2.imwrite('cropwb.jpg', cropwb)
