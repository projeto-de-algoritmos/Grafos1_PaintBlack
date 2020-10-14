import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import tkinter as tk
import sys


def floodFillUtil(screen, x, y, prevC, newC): 
    
    if (x < 0 or x >= M or y < 0 or
    y >= N or (screen[x][y][0] != prevC[0] or screen[x][y][1] != prevC[1] or screen[x][y][2] != prevC[2]) or
    (screen[x][y][0] == newC[0] and screen[x][y][1] == newC[1] and screen[x][y][2] == newC[2]) ): 
        return
    
    prevC = [0,0,0]
    screen[x][y] = newC
    #Pressione enter após setar a cor para ver o algoritmo
    cv2.imshow("Image State", screen)
    cv2.waitKey(0)

    
    floodFillUtil(screen, x + 1, y, prevC, newC) 
    floodFillUtil(screen, x - 1, y, prevC, newC) 
    floodFillUtil(screen, x, y + 1, prevC, newC) 
    floodFillUtil(screen, x, y - 1, prevC, newC) 


def floodFill(screen, x, y, newC):
    prevC = [0,0,0]
    floodFillUtil(screen, x, y, prevC, newC) 



def start():
    
    global root, r_entry, g_entry, b_entry, g_var, r_var, b_var
    root=tk.Tk()

    root.title('Set Color')
    root.geometry("250x125")

    r_var=tk.StringVar() 
    g_var=tk.StringVar() 
    b_var=tk.StringVar()
        

    r_label = tk.Label(root, text = 'RED:',font=('calibre', 10, 'bold')) 
    r_entry = tk.Entry(root, textvariable = r_var,font=('calibre',10,'normal')) 
    
    g_label = tk.Label(root, text = 'GREEN:',font = ('calibre',10,'bold'))
    g_entry=tk.Entry(root, textvariable = g_var, font = ('calibre',10,'normal'))

    b_label = tk.Label(root, text = 'BLUE:', font = ('calibre',10,'bold')) 
    b_entry=tk.Entry(root,textvariable = b_var, font = ('calibre',10,'normal'))

    sub_btn=tk.Button(root,text = 'Submit',command = submit) 
    
    r_label.grid(row=0,column=0) 
    r_entry.grid(row=0,column=1) 
    g_label.grid(row=1,column=0) 
    g_entry.grid(row=1,column=1) 
    b_label.grid(row=2,column=0) 
    b_entry.grid(row=2,column=1) 
    sub_btn.grid(row=3,column=1) 
   
def submit(): 
  
    r=r_entry.get()
    g=g_var.get()
    b=b_var.get() 

    color = [int(b),int(g),int(r)]
    r_var.set("") 
    g_var.set("")
    b_var.set("")
    #fill(img, coordinate, color, N, M)
    print('coordinate:', end=' ')
    print( coordinate)
    floodFill(img, coordinate[0], coordinate[1], color)
    root.destroy()


def takeclick(event, x,y,flags, params):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        global coordinate
        coordinate = [y, x]
        start()
        root.mainloop()


# Abrindo Imagem
origin = cv2.imread('./images/default.png') 

# Redimensionando
scale = 60
width = int(origin.shape[1] * scale / 100)
height = int(origin.shape[0] * scale / 100)

M = width
N = height

new_origin = (width, height)
origin = cv2.resize(origin, new_origin)

gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 2, 200) #Contornando 

img = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)

window = "Image State"
cv2.namedWindow(window)
cv2.setMouseCallback(window, takeclick)

while(True):
    cv2.imshow(window, img)
    if cv2.waitKey(20) == 27:
        break
