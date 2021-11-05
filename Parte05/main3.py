#!/usr/bin/python3

# 2021/11/04 PSR
# BP
# Part 05 -
# Exercício 3
from functools import *
import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
trackbar_name = 'Tresh'
#image_gray = None
alpha_slider_max = 255


def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        print("cordenadas:" + str(x) + ' ' + str(y))


# usando variaveis globais
#def onTrackbar(threshold):
def onTrackbar(image_gray, threshold):

    _, image_thresholded = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_thresholded)


def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-i', '--image', type=str, required=True,help=https://clc.stackoverflow.com/click?an=4ypIX7Z-4_ybHqxHHocEMDGxTNmxQzqbZes68b9T5W-3aTAYM_RsYGBosGdkZGDhZv39QPztXrWD6_Xh4tysO26Izzik9m4zsljzLfHDP5TOvdRGEutZLfW8WfnbF4QYw-zPoveuXBNQNPkCAA&cr=719478&ct=0&url=https%3A%2F%2Fstackoverflow.com%2Fjobs%2Fcompanies%2Fcircle%3Fso_medium%3DAd%26so_source%3DSharedCompanyAd%26so_campaign%3DGenericRed%26med%3Dclc%26clc-var%3D51&sig=9sZQpNW8e9JF8Q'Full path to image file.')
    #args = vars(parser.parse_args())
    #image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    image = cv2.imread("atlascar.png", cv2.IMREAD_COLOR)

   # global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    tonTrackbar = partial(onTrackbar, image_gray)
    #cv2.createTrackbar(trackbar_name, window_name, 0, alpha_slider_max, onTrackbar) #usando variaveis globais
    cv2.createTrackbar(trackbar_name, window_name, 0, alpha_slider_max, tonTrackbar)
    cv2.setMouseCallback(window_name, mouse_callback)
    # Show some stuff
    tonTrackbar(0)
    #onTrackbar(0)              #usando variaveis globais
    # Wait until user press some key

    cv2.waitKey()

if __name__ == '__main__':
    main()