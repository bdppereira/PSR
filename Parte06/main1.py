#!/usr/bin/python3

# 2021/11/04 PSR
# BP
# Part 05 -
# Exercício 3
from functools import *
import argparse
import cv2
import readchar
# Global variables
import numpy as np

window_name = 'window - Ex3a'
trackbar_name = 'Tresh'
#image_gray = None
alpha_slider_max = 255


def mouse_callback(event, x, y, flags, param):
    global img
    global cor

    if event == cv2.EVENT_LBUTTONDOWN:
        print("cordenadas:" + str(x) + ' ' + str(y))
        img[x,y]=(255,0,255)

        if cor == 1:
            cor =(255, 0, 0)
        if cor == 2:
            cor = (0, 255, 0)
        if cor == 3:
            cor = (0, 0, 255)

        centro = (x, y)
        cv2.circle(img, centro, 50, cor, 5)
        cv2.imshow(window_name, img)


def parte1aeb():
    image = cv2.imread("../Parte05/atlascar.png", cv2.IMREAD_COLOR)
    cv2.imshow('original', image)

    a=image.shape[0]
    b = image.shape[1]
    print("altura:" +str(a)+"  largura:"+str(b))
    centro = (int(b/2),int(a/2))

    cv2.circle(image,centro,50,(0,255,0),5)   # Circulo verde no centro

    # texto vermelho no canto
    font=cv2.FONT_HERSHEY_DUPLEX
    posicao = (100, 100)
    fontScale = 2
    fontColor = (0, 0, 255)
    lineType = 2

    cv2.putText(image, 'PSR', posicao, font, fontScale, fontColor, lineType)

    cv2.imshow('circulo', image)

    cv2.waitKey()

def parte1c():

    # Create a black image
    global img
    global cor

    cor = 0
    img = np.zeros((600,400,3), np.uint8)
    img.fill(255)
    sai = 1

    while (sai == 1):

        # pressed_key = readchar.readkey()
        # pressed_key == 'q':  #

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            print("sai")
            sai = 0
        if cv2.waitKey(1) & 0xFF == ord('r'):
            cor = 3
            print("cor r")
        if cv2.waitKey(1) & 0xFF == ord('b'):
            cor = 1
            print("cor b")
        if cv2.waitKey(1) & 0xFF == ord('g'):
            cor = 2
            print("cor g")

        cv2.namedWindow(window_name)
        cv2.imshow(window_name, img)

        cv2.setMouseCallback(window_name, mouse_callback)

    #cv2.waitKey()

    cv2.destroyAllWindows()

def main():
    # parte1aeb()
    parte1c()

if __name__ == '__main__':
    main()