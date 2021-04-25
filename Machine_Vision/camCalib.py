import numpy as np
import cv2 as cv
import glob

### FINDING CORNERS ON CHESSBOARD ###

# checkerboard size
cbSize = (8, 5)
# image size
frameSize = (1920, 1080)

# opencv function to help find the exact corners of the chessboard once detected
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# preparing object points for comparison with optic points
objp = np.zeros((cbSize[0] * cbSize[1],3), np.float32)
objp[:,:2] = np.mgrid[0:cbSize[0], 0:cbSize[1]].T.reshape(-1,2)

# 2 arrays to store object points from all calibration images
objPoints = []      # 3D points in real world space
imgPoints = []      # 2D points in image plane

images = glob.glob('*.png')     # cycles through all images with the file format png

# for each image that is loaded identify corners and store them
for image in images:
    print(image)
    img = cv.imread(image)      # read image and save to variable "img"
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      # convert to grayscale
    success, corners = cv.findChessboardCorners(gray, cbSize, None)     # use opencv function to find corners using the
    # grayscale image previously detected

    # if corners have been successfully detected use the 3d world coordinates that are objPoints to draw corners on
    # each of the images and update the imgPoints with this
    if success == True:

        objPoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)       # find corners in subpixels
        imgPoints.append(corners)       # add optic points to image points

        cv.drawChessboardCorners(img, cbSize, corners2, success)
        cv.imshow('img', img)
        cv.waitKey(1000)        # wait one second until the next image shows

cv.destroyAllWindows()

### CALIBRATION ###

# using all the information from the camera calibration display the different variables to see what is happening
# from the information that has been inputed
success, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objPoints, imgPoints, frameSize, None, None)

print("cam calib: ", success)
print("\nCam Matrix:\n", cameraMatrix)
print("\nDistortion Parameters:\n", dist)
print("\nRotation Vectors:\n", rvecs)
print("\nTranslation Vectors:\n",  tvecs)

### UNDISTORT ###

# optimizes the picture removing distortion
img = cv.imread('cb5.png')
h, w = img.shape[:2]
newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))

# take in image that should be undistorted
dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]     # using slicing the image is cropped
cv.imwrite('caliresult.png', dst)       # save the result of the undistorted cropped image

# Undistort with Remapping
mapx, mapy = cv.initUndistortRectifyMap(cameraMatrix, dist, None, newCameraMatrix, (w,h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('caliResult2.png', dst)

# Reprojection Error
mean_error = 0

# using all vectors, object points, camera matrix and images to get the error rate
for i in range(len(objPoints)):
    imgpoints2, _ = cv.projectPoints(objPoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
    error = cv.norm(imgPoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error

# error rate; how the 2d and 3d points relate to each other and what is the pixel
# detection error based on the camera calibration
print( "total error: {}".format(mean_error/len(objPoints)) )