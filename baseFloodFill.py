# Dimentions of paint screen 
M = 8
N = 8

def floodFillUtil(screen, x, y, prevC, newC): 
	print("prev: %d" % prevC)
	#print(screen[x][y])
	# Casos Triviais
	if (x < 0 or x >= M or y < 0 or
		y >= N or screen[x][y] != prevC	 or
		screen[x][y] == newC): 
		return

	# Recolorindo
	screen[x][y] = newC 
#	print(screen)
	print ("Após aplicar o Balde de Tinta:") 
	for i in range(M): 
		for j in range(N): 
			print(screen[i][j], end = ' ') 
		print()  

	# Colorido os Vizinhos
	floodFillUtil(screen, x + 1, y, prevC, newC) 
	floodFillUtil(screen, x - 1, y, prevC, newC) 
	floodFillUtil(screen, x, y + 1, prevC, newC) 
	floodFillUtil(screen, x, y - 1, prevC, newC)

# Função Inicial
def floodFill(screen, x, y, newC): 
	prevC = screen[x][y] 
	floodFillUtil(screen, x, y, prevC, newC) 

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
print(screen[x][y])
floodFill(screen, x, y, newC) 

print ("Após aplicar o Balde de Tinta:") 
for i in range(M): 
	for j in range(N): 
		print(screen[i][j], end = ' ') 
	print()  
