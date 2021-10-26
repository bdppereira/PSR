#!/usr/bin/python3

# 2021/10/26 PSR
# BP
# Part 03 - # 2021/10/21 PSR
# Exercício 1 - Tempo e Temporizadores

from colorama import Fore, Back, Style
import time
import math
nmax = 5000000

def tic():
    return time.time()

def toc( inicio):
    return time.time() - inicio

def main():

    inicio = tic()

    seconds = time.time()
    local_time = time.ctime(seconds)
    print("This is" + Fore.RED +"Ex1"+ Style.RESET_ALL+" Local time:" + Fore.BLUE + Back.GREEN + local_time + Style.RESET_ALL)

    #time.sleep(2)

    for i in range(1, nmax):
        result = math.sqrt(i)

    fim = toc(inicio)

    print('Ellapsed time: ', fim)


if __name__ == '__main__':
    main()



