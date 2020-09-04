import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(10**7)
print(sys.getrecursionlimit())

M = 8
N = 8

def floodFillUtil(screen, x, y, prevC, newC): 
    #print(prevC)
    prevC = [0,0,0]
    #prevC = screen[x][y]
    #print(screen[x][y][0] != prevC[0] or screen[x][y][1] != prevC[1] or screen[x][y][2] != prevC[2])
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
    print(prevC)
    floodFillUtil(screen, x, y, prevC, newC) 






def fill(screen, start_coords, fill_value, i, j):
    #xsize, ysize = screen.shape
    xsize = j
    ysize = i
    orig_value = screen[start_coords[0]][start_coords[1]]
    print(orig_value)
    print(fill_value)
    stack = set(((start_coords[0], start_coords[1]),))
    if fill_value[0] == orig_value[0] and fill_value[1] == orig_value[1] and fill_value[2] == orig_value[2] :
        raise ValueError("Filling region with same value "
                        "already present is unsupported. "
                        "Did you already fill this region?")

    while stack:
        orig_value = [0,0,0]
        x, y = stack.pop()

        if screen[x][y][0] == orig_value[0] and screen[x][y][1] == orig_value[1] and screen[x][y][2] == orig_value[2]:
            screen[x][y] = fill_value
            cv2.imshow("Image", screen)
            cv2.waitKey(0)
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))



origin = cv2.imread('./images/naruto.jpg') #load naruto image 
#gray = cv2.imread('captchas/download.png', 0) # Open image in gray scale

#Re-Escale Image by Proportion
scale = 50
width = int(origin.shape[1] * scale / 100)
height = int(origin.shape[0] * scale / 100)
#print(width, height)

M = width
N = height

new_origin = (width, height)

origin = cv2.resize(origin, new_origin)
cv2.imshow('naruto', origin)
#print (origin)

gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
cv2.imshow('Naruto Gray', gray)

gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 2, 200)
cv2.imshow('Naruto Cinza', edged)
cv2.waitKey(0)
img = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)

y = 239
x = 164
color = [0,0,255]
coordinate = [x, y]

fill(img, coordinate, color, N, M)

#print(img[0][0] == color)

#floodFill(img, x, y, color)
#cv2.imshow('Narutin', img)
#cv2.waitKey(0)

"""
y = 294
x = 168
color = [255,50,50]
#print(img[0][0] == color)

floodFill(img, x, y, color)
cv2.imshow('Narutin2', img)
cv2.waitKey(0)



y = 205
x = 194
color = [125,125,125]
#print(img[0][0] == color)

floodFill(img, x, y, color)
cv2.imshow('Narutin3', img)
cv2.waitKey(0)



y = 177
x = 414
color = [0,0,255]
#print(img[0][0] == color)

floodFill(img, x, y, color)
cv2.imshow('Narutin4', img)
cv2.waitKey(0)
"""

"""
for i in img:
    for j in range(len(i)):
        i[j][0] = 000 #B
        i[j][1] = 000 #G
        i[j][2] = 139 #R
"""

