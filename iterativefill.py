def fill(screen, start_coords, fill_value):
    #xsize, ysize = screen.shape
    xsize = 8
    ysize = 8
    orig_value = screen[start_coords[0]][start_coords[1]]
    print("original: %d" % orig_value)
    stack = set(((start_coords[0], start_coords[1]),))
    if fill_value == orig_value:
        raise ValueError("Este segmento de imagem ja possui esta cor"
                        "Ja está colorido\n")

    while stack:
        #print("ok")
        x, y = stack.pop()
 
        if screen[x][y] == orig_value:
            screen[x][y] = fill_value
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))

                

# "Main"
screen = [[1, 1, 1, 1, 1, 1, 1, 1], 
		[1, 1, 1, 1, 1, 1, 0, 0], 
		[1, 0, 0, 1, 1, 0, 1, 1], 
		[1, 2, 2, 2, 2, 0, 1, 0], 
		[1, 1, 1, 2, 2, 0, 1, 0], 
		[1, 1, 1, 2, 2, 2, 2, 0], 
		[1, 1, 1, 1, 1, 2, 1, 1], 
		[1, 1, 1, 1, 1, 2, 2, 1]] 

x = 0
y = 0
newC = 3
coord = [x, y]
fill(screen, coord, newC) 

print ("Após aplicar o Balde de Tinta:") 
for i in range(8): 
	for j in range(8): 
		print(screen[i][j], end = ' ') 
	print()  
