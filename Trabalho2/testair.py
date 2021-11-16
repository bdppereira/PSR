#!/usr/bin/python3

# 2021/11/11 PSR

import json
from functools import *
import argparse
import cv2
import numpy as np
import json
from pprint import pprint

window_name = 'airpaint'
window_name_mask = 'airpaintmask'

def main():

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------
    capture = cv2.VideoCapture(0)  # setup video capture for webcam
    # capture = cv2.VideoCapture('test2.mp4')  # setup video capture from video file

    # configure opencv window
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # -----------------------------------------------------
    # EXECUTION
    # -----------------------------------------------------

    with open('./limits.json') as data_file:
        ranges = json.load(data_file)

    #print(ranges)

    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])

    _, image = capture.read()  # get an image from the camera

    height, width, _ = image.shape
    paintbrush = np.ndarray((height, width), dtype=np.uint8)  # create a mask same size as image
    paintbrush.fill(255)  # set image to all zeros

    while True:
        _, image = capture.read()  # get an image from the camera

        mask = cv2.inRange(image, mins, maxs)

        #_, thresh = cv2.threshold(mask, 225, 255, cv2.THRESH_BINARY)  #THRESH_BINARY_INV
        kernal = np.ones((2, 2), np.uint8)
        #dilation = cv2.dilate(thresh, kernal, iterations=2)
        dilation = cv2.dilate(mask, kernal, iterations=2)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        objects = str(len(contours))

        # erode and then dilate is the same as opening
        dilation = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernal)
        contour, _ = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        sorted_ctrs = sorted(contour, key=lambda ctr: cv2.boundingRect(ctr)[1])
        for i, ctr in enumerate(sorted_ctrs):
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            break;
        # # And draw it on the original image
        # for c in contour:
        #     # enter your filtering here
        #     x, y, w, h = cv2.boundingRect(c)
        #     # para experimentar desenha na imagem original
        #     #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #
        #     # for contour in contours:
        #     #     if cv2.contourArea(contour) < 80:
        #     #
        #     # for contour in contours:
        #     #     rect = cv2.boundingRect(contour)
        #     #     area = rect[2] * rect[3]

        cv2.imshow(window_name, image)
        cv2.imshow(window_name_mask, mask)
        cv2.imshow('paintbrush', dilation)


        if image is None:
            print('Video is over, terminating.')
            break  # video is over

        key = cv2.waitKey(20)
        if key == ord('q'):  # q for quit
            print('You pressed q ... aborting')
            break


if __name__ == '__main__':
    main()


