#!/usr/bin/python3

# 2021/11/11 PSR

import json
from functools import *
import argparse
import cv2
import numpy as np
import copy
import colorama


# Global variables
window_name_org = 'LiveWindow'
window_name_alt = 'MixWindow'
trackbar_minBH = 'min B/H'
trackbar_maxBH = 'max B/H'
trackbar_minGS = 'min G/S'
trackbar_maxGS = 'max G/S'
trackbar_minRV = 'min R/V'
trackbar_maxRV = 'max R/V'
file_name = './limits.json'

#image_gray = None
alpha_slider_min = 0
alpha_slider_max = 255

file_name = 'limits.json'

def nothing(x):
    pass


def main():
   # parser = argparse.ArgumentParser()
   #  parser.add_argument('-c', '--cor', type=str, required=True,help='Full path to image file.')
   #  args = vars(parser.parse_args())

    capture = cv2.VideoCapture(0)  # setup video capture for webcam
    # configure opencv window
    cv2.namedWindow(window_name_org, cv2.WINDOW_AUTOSIZE)

    _, image = capture.read()
    cv2.imshow(window_name_org, image)
    cv2.imshow(window_name_alt, image)

    cv2.createTrackbar(trackbar_minBH, window_name_alt, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_maxBH, window_name_alt, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_minGS, window_name_alt, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_maxGS, window_name_alt, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_minRV, window_name_alt, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_maxRV, window_name_alt, alpha_slider_min, alpha_slider_max, nothing)

    while True:
        _, image = capture.read()  # get an image from the camera

        if image is None:
            print('Video is over, terminating.')
            break  # video is over

        cv2.imshow(window_name_org, image)
w
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('w'):
            with open(file_name, 'w') as file_handle:
                print('writing dictionary range to file ' + file_name)
                json.dump(ranges, file_handle)  # d is the dicionary
                file_handle.close()
            break

        minBH = cv2.getTrackbarPos(trackbar_minBH, window_name_alt)
        maxBH = cv2.getTrackbarPos(trackbar_maxBH, window_name_alt)
        minGS = cv2.getTrackbarPos(trackbar_minGS, window_name_alt)
        maxGS = cv2.getTrackbarPos(trackbar_maxGS, window_name_alt)
        minRV = cv2.getTrackbarPos(trackbar_minRV, window_name_alt)
        maxRV = cv2.getTrackbarPos(trackbar_maxRV, window_name_alt)

        ranges = {'b': {'min': int(minBH), 'max': int(maxBH)},
                  'g': {'min': int(minGS), 'max': int(maxGS)},
                  'r': {'min': int(minRV), 'max': int(maxRV)} }

        mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
        maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])

        #print (mins)
        #print (maxs)

        imager = cv2.inRange(image, mins, maxs)

        cv2.imshow(window_name_alt, imager)

    #cv2.waitKey()
    cv2.destroyAllWindows()

    # with open(file_name, 'w') as file_handle:
    #     print('writing dictionary d to file ' + file_name)
    #     json.dump(ranges, file_handle) # d is the dicionary
    #     file_handle.close()





if __name__ == '__main__':
    main()