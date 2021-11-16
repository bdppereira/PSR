#!/usr/bin/python3

# 2021/11/04 PSR
# BP
# Part 05 -
# Exercício 3
import copy
from functools import *
import argparse

import colorama
import cv2
import numpy as np



def video():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'

    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    image_previous = None

    while (True):
        success, image = capture.read()  # get an image from the camera
        image_gui = copy.deepcopy(image)
        #cv2.imshow(window_name, image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if image_previous is None:
            image_previous = copy.deepcopy(img_gray)

        height, width, _ = image.shape
        mask_mouth = np.ndarray((height, width), dtype=np.int8)
        mask_mouth.fill(0)

        mask_face = np.ndarray((height, width), dtype=np.int8)
        mask_face.fill(0)

        faces = face_cascade.detectMultiScale(img_gray, 1.1, 6)

        for x, y, w, h in faces:

            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # Mascara com tudo a preto e depois o rectangulo da cara a branco
            mask_face = cv2.rectangle(mask_face, (x, y), (x + w, y + h), 255, -1)

            cv2.add(image, (-10, 100, -10, 0), dst=image_gui, mask=mask_face) # pintar o rectangulo de verde

           # cv2.rectangle(image_gui, (x, y + (2 * round(h / 3))), (x + w, y + h - (round(h / 11))), (0, 0, 255), 3)
            mask_face = cv2.rectangle(mask_face, (x, y), (x + w, y + h), 255, -1)  # draw blue rectangle around face

            # Mascara com tudo a preto e depois o rectangulo da boca a branco
            #mask_mouth = cv2.rectangle(mask_mouth, (x, y + (2 * round(h / 3))), (x + w, y + h - (round(h / 11))), 255, -1)
            mask_mouth = cv2.rectangle(mask_mouth, (x, int(y + h - round(h / 3))), (x + w, y + h), 255, -1)
            #
            # image_gui[mask_mouth.astype(bool)] = (255,255,0)
            # cv2.add(image_gui, (-10,50,-10,0),dst=image_gui, mask=mask_mouth)

            diff=cv2.absdiff(img_gray, image_previous) * (mask_mouth/255)
            total = np.sum(diff)
            print(total)
            if total > 15000:
                print(colorama.Fore.RED + 'Mouth is moving ' + colorama.Style.RESET_ALL)

            cv2.imshow(window_name, image_gui)
            cv2.imshow("diff", diff)
            cv2.imshow("mask_mouth", mask_mouth)

        image_previous = copy.deepcopy(img_gray)

    #cv2.imwrite('main2.jpg', image)

    capture.release()
    cv2.destroyAllWindows()


def imagem():
    img = cv2.imread('main2.jpg')
    # Display original image
    cv2.imshow('Original', img)
    cv2.waitKey(0)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  # Combined X and Y Sobel Edge Detection
    # Display Sobel Edge Detection Images
    cv2.imshow('Sobel X', sobelx)
    cv2.imshow('Sobel Y', sobely)
    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    cv2.waitKey(0)

    # Canny Edge Detection

    edges = cv2.Canny(image=img_blur, threshold1=200, threshold2=200)  # Canny Edge Detection original 100 200

    # Disy Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imagemFace():

    img = cv2.imread('main2.jpg')
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    image_gui = copy.deepcopy(img)
    height, width, _ = img.shape
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(img_gray, 1.1, 6)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)


       #x:607   y:120   w:403   h:403
    #   print('x:'+str(x)+'   y:'+str(y)+'   w:'+str(w)+'   h:'+str(h))
        cv2.imshow('Face Detector', img)

        mask_mouth = np.ndarray((height,width), dtype=np.int8)
        mask_mouth.fill(0)
        mask_mouth = cv2.rectangle(mask_mouth, (x, y + (2 * int(h / 3))), (x + w, y + h - (int(h / 9))), (0, 0, 255), 3)

        cv2.imshow('mask_mouth', mask_mouth)

        image_gui[mask_mouth.astype(bool)] = (255,255,0)
        cv2.add(img, (-10,50,-10,0),dst=image_gui, mask=mask_mouth)
        cv2.imshow('image_gui', image_gui)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    video()
    #imagem()
    #imagemFace()

if __name__ == '__main__':
    main()

