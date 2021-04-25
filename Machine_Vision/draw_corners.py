#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import os
import glob
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse

#def main():
    # termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def calibrate(dirpath, prefix, image_format, square_size, width=9, height=6):
    """ Apply camera calibration operation for images in the given directory path. """
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(8,6,0)
    objp = np.zeros((height*width, 3), np.float32)
    objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

    objp = objp * square_size # if square_size is 1.5 centimeters, it would be
    # better to write it as 0.015 meters. Meter is a better metric because most
    # of the time we are working on meter level projects.

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.# Some people will add "/"
    #character to the end. It may brake the code so I wrote a check.
    if dirpath[-1:] == '/':
        dirpath = dirpath[:-1]

    images = glob.glob(dirpath+'/' + prefix + '*.'+ image_format)

    for fname in images:
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (width, height), None)

        # If found, add object points, image points (after refining them)
        if ret:
            objpoints.append(objp)

            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv.drawChessboardCorners(img, (width, height), corners2, ret)
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints,
        gray.shape[::-1], None, None)

    return [ret, mtx, dist, rvecs, tvecs]

def save_coefficients(mtx, dist, path):
    """ Save the camera matrix and the distortion coefficients to given path/file. """
    cv_file = cv.FileStorage(path, cv.FILE_STORAGE_WRITE)
    cv_file.write("K", mtx)
    cv_file.write("D", dist)
    # note you *release* you don't close() a FileStorage object
    cv_file.release()

def load_coefficients(path):
    """ Loads camera matrix and distortion coefficients. """
    # FILE_STORAGE_READ
    cv_file = cv.FileStorage(path, cv.FILE_STORAGE_READ)

    # note we also have to specify the type to retrieve other wise we only get a
    # FileNode object back instead of a matrix
    camera_matrix = cv_file.getNode("K").mat()
    dist_matrix = cv_file.getNode("D").mat()

    cv_file.release()
    return [camera_matrix, dist_matrix]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Camera calibration')
    parser.add_argument('/Jenga/Pics_n_Vids/chessboard', type=str, required=True, help='image directory path')
    parser.add_argument('png', type=str, required=True,  help='image format, png/jpg')
    parser.add_argument('cb', type=str, required=True, help='image prefix')
    parser.add_argument('0.03', type=float, required=False, help='chessboard square size')
    parser.add_argument('9', type=int, required=False, help='chessboard width size, default is 9')
    parser.add_argument('6', type=int, required=False, help='chessboard height size, default is 6')
    parser.add_argument('YML', type=str, required=True, help='YML file to save calibration matrices')

    args = parser.parse_args()
    ret, mtx, dist, rvecs, tvecs = calibrate(args.image_dir, args.prefix, args.image_format, args.square_size, args.width, args.height)
    save_coefficients(mtx, dist, args.save_file)
    print("Calibration is finished. RMS: ", ret)

#===============================================================================

# termination criteria
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#
# # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# objp = np.zeros((6*7,3), np.float32)
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
#
# # Arrays to store object points and image points from all the images.
# objpoints = [] # 3d point in real world space
# imgpoints = [] # 2d points in image plane.
# images = glob.glob('Pics_n_Vids/chessboard/chessboard1.png')
#
# for fname in images:
#     img = cv.imread(fname)
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # Find the chess board corners
#     ret, corners = cv.findChessboardCorners(gray, (7,6), None)
#     # If found, add object points, image points (after refining them)
#     if ret == True:
#         objpoints.append(objp)
#         corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
#         imgpoints.append(corners)
#         # Draw and display the corners
#         cv.drawChessboardCorners(img, (7,6), corners2, ret)
#         cv.imshow('img', img)
#         cv.waitKey(500)
# cv.destroyAllWindows()

#===============================================================================

# prepare object points
# nx = 18 #number of inside corners in x
# ny = 13 #number of inside corners in y
#
# # Make a list of calibration images
# fname = 'chessboard1.png'
# img = cv.imread(fname)
#
# # Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# # Find the chessboard corners
# ret, corners = cv.findChessboardCorners(gray, (nx, ny), None)
#
# # If found, draw cornerss
# if ret == True:
#     # Draw and display the corners
#     cv.drawChessboardCorners(img, (nx, ny), corners, ret)
#     plt.imshow(img)
