#!/usr/bin/python3

# 2021/10/26 PSR
# BP
# Part 03 - # 2021/10/27 PSR
# EExercício 3 - Named Tuples

from colorama import Fore, Back, Style
import time
import math

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def tic():
    return time.time()

def toc( inicio):
    return time.time() - inicio

# (a+bi) + (c+di) = (a+c) + (b+d)i
def addComplex(x, y):
    SomaR = x.r + y.r
    SomaI = x.i + y.i

    return Complex(SomaR, SomaI)

# (a+bi)(c+di) = ac + adi + bci + bdi2
def multiplyComplex(x, y):
    SomaR = x.r * y.r
    SomaI1 = x.r * y.i
    SomaI2 = x.i * y.r
    SomaII = (x.i * y.i) * -1

    #print("x.r  :" + str(x.r ) + "  y.r :" + str(y.r) + "  y.i :" + str(y.i) + "  x.i :" + str(x.i))
    #print("SomaR :" + str(SomaR) + "  SomaII :" + str(SomaII) + "  SomaI1 :" + str(SomaI1) + "  SomaI2 :" + str(SomaI2)  )

    return Complex(SomaR + SomaII, SomaI1 + SomaI2)

def printComplex(x):
    print("Nº Complexo :" +str(x.r) + " + i "+str(x.i) )


def main():
    inicio = tic()

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1))  # named tuple looks nice when printed

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


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




if __name__ == '__main__':
    main()