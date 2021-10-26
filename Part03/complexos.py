#!/usr/bin/python3

# 2021/10/26 PSR
# BP
# Part 03 - # 2021/10/21 PSR
# Exercício 2 - Números complexos

from colorama import Fore, Back, Style
import time
import math

def tic():
    return time.time()

def toc( inicio):
    return time.time() - inicio

# (a+bi) + (c+di) = (a+c) + (b+d)i
def addComplex(x, y):
    SomaR = x[0] + y[0]
    SomaI = x[1] + y[1]
    return (SomaR, SomaI)

# (a+bi)(c+di) = ac + adi + bci + bdi2
def multiplyComplex(x, y):
    SomaR = x[0] * y[0]
    SomaI1 = x[0] * y[1]
    SomaI2 = x[1] * y[0]
    SomaII = (x[1] * y[1]) * -1
   # print("SomaR :" + str(SomaR) + "  SomaII :" + str(SomaII) + "  SomaI1 :" + str(SomaI1) + "  SomaI2 :" + str(SomaI2)  )

    return (SomaR + SomaII, SomaI1 + SomaI2)

def printComplex(x):
    print("Nº Complexo :" +str(x[0]) + "+ i"+str(x[1]) )


def main():
    inicio = tic()

    # ex2 a)
    # define two complex numbers as tuples of size two
    #c1 = (5, 3)
    #c2 = (-2, 7)
    # Resultado
    # Nº Complexo :3+ i10
    # Nº Complexo :-7+ i13

   # c1 = (3, 2)
   # c2 = (1, 7)
    # Resultado
   # Nº Complexo: 4 + i9
   # Nº Complexo: -11 + i23

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()
