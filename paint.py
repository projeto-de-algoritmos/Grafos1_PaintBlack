import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000000)


M = 8
N = 8

def floodFillUtil(screen, x, y, prevC, newC): 
    #print(prevC)
    prevC = [0,0,0]
    #prevC = screen[x][y]
    #print(screen[x][y][0] != prevC[0] and screen[x][y][1] != prevC[1] and screen[x][y][2] != prevC[2])
    # Base cases 
    if (x < 0 or x >= M or y < 0 or
    y >= N or (screen[x][y][0] != prevC[0] or screen[x][y][1] != prevC[1] or screen[x][y][2] != prevC[2]) or
    (screen[x][y][0] == newC[0] and screen[x][y][1] == newC[1] and screen[x][y][2] == newC[2]) ): 
        return
    prevC = screen[x][y]

    # Replace the color at (x, y) 
    screen[x][y] = newC
    #print(screen[x][y])
    cv2.imshow("sasuke", screen)
    cv2.waitKey(0)

    #
    # Recur for north, east, south and west 
    print("1")
    #print(x)
    floodFillUtil(screen, x + 1, y, prevC, newC) 
    print("2")
    floodFillUtil(screen, x - 1, y, prevC, newC) 
    print("3")
    floodFillUtil(screen, x, y + 1, prevC, newC) 
    print("4")
    floodFillUtil(screen, x, y - 1, prevC, newC) 


def floodFill(screen, x, y, newC): 
    prevC = screen[x][y]
    print("ok")
    floodFillUtil(screen, x, y, prevC, newC) 




origin = cv2.imread('./images/naruto.jpg') #load naruto image 
#gray = cv2.imread('captchas/download.png', 0) # Open image in gray scale

#Re-Escale Image by Proportion
scale = 50
width = int(origin.shape[1] * scale / 100)
height = int(origin.shape[0] * scale / 100)
#print(width, height)
M = 240
N = 320

new_origin = (width, height)

origin = cv2.resize(origin, new_origin)
cv2.imshow('naruto', origin)

#print (origin)

gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
cv2.imshow('Naruto Gray', gray)

gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Naruto Cinza', edged)

img = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)
"""
for i in img:
    for j in range(len(i)):
        i[j][0] = 000 #B
        i[j][1] = 000 #G
        i[j][2] = 139 #R
"""

x = 167
y = 253
color = [128,0,128]
#print(img[0][0] == color)

floodFill(img, x, y, color)
cv2.imshow('Narutin', img)
cv2.waitKey(0)

