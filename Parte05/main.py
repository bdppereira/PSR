#!/usr/bin/python3

# 2021/11/03 PSR
# BP
# Part 05 - # 2021/11/03 PSR
# Exercício 1 a) - Leitura de imagens

import cv2
import argparse
import numpy as np
op = 1
# ./main.py -fto atlascar2.png

def exerc1():
    if op == 2:
        image_filename =args.get('file_to_open')  # 'atlascar2.png'
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(0) # wait for a key press before proceeding

    if op == 1:
        image_filename =  'atlascar.png'
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image

        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(3000)  # wait for a key press before proceeding

        cv2.destroyAllWindows()
        image_filename = 'atlascar2.png'
        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image

        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(3000)  # wait for a key press before proceeding


def exerc2():
    image_filename = 'atlascar2.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
    #retval, image_thresholded = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)
    retval, image_thresholded = cv2.threshold(image, 150, 200, cv2.THRESH_BINARY) #cv2.THRESH_BINARY

    cv2.imshow('tresh', image_thresholded)  # Display the image
    cv2.waitKey(1000)  # wait for a key press before proceeding

    imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', imagegray)

    #print(type(image.shape))

    (B, G, R) = cv2.split(image)
    # show each channel individually
    cv2.imshow("Red", R)
    retval, image_B_thresholded = cv2.threshold(B, 50, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY
    retval, image_G_thresholded = cv2.threshold(G, 100, 255, cv2.THRESH_BINARY)
    retval, image_R_thresholded = cv2.threshold(R, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow("image_B_thresholded", image_B_thresholded)
    cv2.imshow("image_G_thresholded", image_G_thresholded)
    cv2.imshow("image_R_thresholded", image_R_thresholded)

    #cv2.imshow('tred', image_thresholded)
    #cv2.imshow("Green", G)
    #cv2.imshow("Blue", B)

    cv2.waitKey(0)

   #Binarisar canais  (b=50, g=100, r=150).

    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)

    merged_tresh = cv2.merge([image_B_thresholded, image_G_thresholded, image_R_thresholded])
    cv2.imshow("merged_tresh", merged_tresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# visualize each channel in color
#zeros = np.zeros(image.shape[:2], dtype="uint8")
#cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
#cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
#cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
#cv2.waitKey(0)

def exerc2d():
    ## Read

    print("2D")

    img = cv2.imread("atlas2000_e_atlasmv.png")

    #(B, G, R) = cv2.split(img)

    ranges = {'b': {'min':0, 'max':50},
              'g': {'min': 90, 'max': 256},
              'r': {'min': 0, 'max': 60} }

    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    image_processed = cv2.inRange(img, mins, maxs)

    cv2.namedWindow("original", cv2.WINDOW_GUI_NORMAL )
    cv2.imshow("original", img)
    cv2.imshow("processada", image_processed)

    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,0,0) ~ (70, 255,255)
    mask1 = cv2.inRange(hsv, (36, 90, 90), (70, 255,255))
    cv2.imshow("hsvmask1", mask1)

    #cv2.imshow("mask2", mask2)
    #cv2.waitKey(0)
    ## final mask and masked
    #mask = cv2.bitwise_or(mask1, mask2)
    #target = cv2.bitwise_and(img,img, mask=mask)

    #cv2.imshow("mask", mask)    #cv2.waitKey(0)    #cv2.imwrite("target.png", target)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def exerc2f():
    ## Read
    img = cv2.imread("atlas2000_e_atlasmv.png")

    (B, G, R) = cv2.split(img)

    ranges = {'b': {'min':0, 'max':70},
              'g': {'min': 90, 'max': 256},
              'r': {'min': 0, 'max': 70} }

    print (ranges)

    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(img, mins, maxs)

    cv2.imshow("processada", mask)

    mask = mask.astype(np.bool)
    img[mask] = (255,0,0)

    cv2.namedWindow("original", cv2.WINDOW_GUI_NORMAL )
    cv2.imshow("original", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description='Definitions of test mode')
    parser.add_argument('-fto', '--file_to_open', type = str, help='ficheiro de imagem a abrir') #required = true

    global args
    args = vars(parser.parse_args())

    if args.get('file_to_open') is None:  # Verifica se o argumento max_value está preenchido.
       op = 1
    else:
       op = 2

    # exerc2d()

    exerc2f()

    print("FIM")

if __name__ == '__main__':
    main()