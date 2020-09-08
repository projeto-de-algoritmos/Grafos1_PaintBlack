import cv2
import tkinter as tk
import sys


def start():
    
    global root, r_entry, g_entry, b_entry, g_var, r_var, b_var
    root=tk.Tk()

    root.title('Set Color')
    root.geometry("250x125")

    r_var=tk.StringVar() 
    g_var=tk.StringVar() 
    b_var=tk.StringVar()
        

    r_label = tk.Label(root, text = 'R:',font=('calibre', 10, 'bold')) 
    r_entry = tk.Entry(root, textvariable = r_var,font=('calibre',10,'normal')) 
    
    g_label = tk.Label(root, text = 'G:',font = ('calibre',10,'bold'))
    g_entry=tk.Entry(root, textvariable = g_var, font = ('calibre',10,'normal'))

    b_label = tk.Label(root, text = 'B:', font = ('calibre',10,'bold')) 
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
    fill(img, coordinate, color, N, M)
    root.destroy()


def takeclick(event, x,y,flags, params):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,y)
        global coordinate
        coordinate = [y, x]
        #color = list(map(int,input("Por favor insira os valores RGB(Ex: 255 255 125): ").strip().split()))
        start()
        root.mainloop()

    


def fill(screen, start_coords, fill_value, i, j):
    xsize = i
    ysize = j
    orig_value = screen[start_coords[0]][start_coords[1]]
    print(orig_value)
    print(fill_value)
    stack = set(((start_coords[0], start_coords[1]),))
    if fill_value[0] == orig_value[0] and fill_value[1] == orig_value[1] and fill_value[2] == orig_value[2] :
        raise ValueError("Esta região ja está colorida com a cor solicitada\n")

    while stack:
        orig_value = [0,0,0]
        x, y = stack.pop()

        if screen[x][y][0] == orig_value[0] and screen[x][y][1] == orig_value[1] and screen[x][y][2] == orig_value[2]:
            screen[x][y] = fill_value
            cv2.imshow("Image State", screen)
            cv2.waitKey(1)
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))


#Main
origin = cv2.imread('./images/default.png') #load image 

#Re-Escale Image by Proportion
scale = 80
width = int(origin.shape[1] * scale / 100)
height = int(origin.shape[0] * scale / 100)

M = width
N = height

new_origin = (width, height)
origin = cv2.resize(origin, new_origin)
#cv2.imshow('inicial', origin)

gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 2, 200)
#cv2.imshow('bordas e arestas', edged)

img = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)

window = "Image State"
cv2.namedWindow(window)
cv2.setMouseCallback(window, takeclick)

while(True):
    cv2.imshow(window, img)
    if cv2.waitKey(20) == 27:
        break