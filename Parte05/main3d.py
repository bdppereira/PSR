#!/usr/bin/python3

# 2021/11/04 PSR
# BP
# Part 05 -
# Exercício 3
import json
from functools import *
import argparse
import cv2
import numpy as np

# Global variables
window_name = 'window - Ex3a'
trackbar_minBH = 'min B/H'
trackbar_maxBH = 'max B/H'
trackbar_minGS = 'min G/S'
trackbar_maxGS = 'max G/S'
trackbar_minRV = 'min R/V'
trackbar_maxRV = 'max R/V'

#image_gray = None
alpha_slider_min = 0
alpha_slider_max = 255

file_name = 'limits.json'

def nothing(x):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cor', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread("atlascar.png")  # , cv2.IMREAD_COLOR)

    #print(" mode ::" + args['cor']+"::" )

    if ((args['cor']) == 'HSV'):
        print("HSV mode")
        trata = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    else:
        print("RGB mode")
        trata = cv2.imread("atlascar.png") #, cv2.IMREAD_COLOR)

    cv2.imshow('original', trata)
    imager = trata
    image = trata

    # global image_gray # use global var
    #image_gray = cv2.cvtColor(image, cv2.)  # convert bgr to gray image (single channel) COLOR_BGR2GRAY
    cv2.namedWindow(window_name)

 #   tonTrackbar = partial(onTrackbar, image)
    cv2.createTrackbar(trackbar_minBH, window_name, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_maxBH, window_name, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_minGS, window_name, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_maxGS, window_name, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_minRV, window_name, alpha_slider_min, alpha_slider_max, nothing)
    cv2.createTrackbar(trackbar_maxRV, window_name, alpha_slider_min, alpha_slider_max, nothing)

    while(1):

        cv2.imshow(window_name, imager)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        minBH = cv2.getTrackbarPos(trackbar_minBH, window_name)
        maxBH = cv2.getTrackbarPos(trackbar_maxBH, window_name)
        minGS = cv2.getTrackbarPos(trackbar_minGS, window_name)
        maxGS = cv2.getTrackbarPos(trackbar_maxGS, window_name)
        minRV = cv2.getTrackbarPos(trackbar_minRV, window_name)
        maxRV = cv2.getTrackbarPos(trackbar_maxRV, window_name)

        #print('VALROES::'+ str(minBH) + '  ' + str(maxBH) +'  GS::' + str(minGS) +'  ' + str(maxGS)+'  RV::' + str(minRV) +'  ' + str(maxRV) )

        ranges = {'b': {'min': int(minBH), 'max': int(maxBH)},
                  'g': {'min': int(minGS), 'max': int(maxGS)},
                  'r': {'min': int(minRV), 'max': int(maxRV)} }

        mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
        maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])

        #print (mins)
        #print (maxs)

        imager = cv2.inRange(image, mins, maxs)


    #cv2.waitKey()
    cv2.destroyAllWindows()

    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(ranges, file_handle) # d is the dicionary
        file_handle.close()


if __name__ == '__main__':
    main()