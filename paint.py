import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import sys

#sys.setrecursionlimit(10**7)
#print(sys.getrecursionlimit())


def floodFillUtil(screen, x, y, prevC, newC): 
    prevC = [0,0,0]
    
    if (x < 0 or x >= M or y < 0 or
    y >= N or (screen[x][y][0] != prevC[0] or screen[x][y][1] != prevC[1] or screen[x][y][2] != prevC[2]) or
    (screen[x][y][0] == newC[0] and screen[x][y][1] == newC[1] and screen[x][y][2] == newC[2]) ): 
        return
    
    prevC = screen[x][y]
    screen[x][y] = newC
    #cv2.imshow("sasuke", screen)
    #cv2.waitKey(0)

    
    floodFillUtil(screen, x + 1, y, prevC, newC) 
    floodFillUtil(screen, x - 1, y, prevC, newC) 
    floodFillUtil(screen, x, y + 1, prevC, newC) 
    floodFillUtil(screen, x, y - 1, prevC, newC) 


def floodFill(screen, x, y, newC): 
    floodFillUtil(screen, x, y, prevC, newC) 


def takeclick(event, x,y,flags, params):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        coordinate = [y, x]
        counter = 0
        fill(img, coordinate, color, N, M)


def fill(screen, start_coords, fill_value, i, j):
    xsize = i
    ysize = j
    orig_value = screen[start_coords[0]][start_coords[1]]
    print(orig_value)
    print(fill_value)
    stack = set(((start_coords[0], start_coords[1]),))
    if fill_value[0] == orig_value[0] and fill_value[1] == orig_value[1] and fill_value[2] == orig_value[2] :
        raise ValueError("Está região ja está colorida com a cor solicitada\n")

    while stack:
        orig_value = [0,0,0]
        x, y = stack.pop()

        if screen[x][y][0] == orig_value[0] and screen[x][y][1] == orig_value[1] and screen[x][y][2] == orig_value[2]:
            screen[x][y] = fill_value
            cv2.imshow("Aplicando Flood Fill", screen)
            cv2.waitKey(1)
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))
    




origin = cv2.imread('./images/naruto.jpg') #load naruto image 

#Re-Escale Image by Proportion
scale = 60
width = int(origin.shape[1] * scale / 100)
height = int(origin.shape[0] * scale / 100)
#print(width, height)

M = width
N = height

new_origin = (width, height)

origin = cv2.resize(origin, new_origin)
#cv2.imshow('naruto', origin)
#print (origin)

gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Naruto Gray', gray)

gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 2, 200)
#cv2.imshow('Naruto Cinza', edged)
#cv2.waitKey(0)

img = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)

window = "Image State"
cv2.namedWindow(window)

color = [255,50,50]
cv2.setMouseCallback(window, takeclick)

#color = list(map(int,input("Por favor insira os valores RGB(Ex: 255 255 125): ").strip().split()))    
    
counter = 0
while(True):
    cv2.imshow(window, img)
    if cv2.waitKey(20) == 27:
        break