# title : pygame-draw-rect
# author : Sam Genoguin 
# country : Philippines

# importing needed modules
import pygame
import sys
import random

# declaring screen, clock and condition
screen = pygame.display.set_mode((720, 1404))
clock = pygame.time.Clock()
running = True

# function to add texts
def addText(text, color, fontsize):
	pygame.font.init()
	Font = pygame.font.SysFont("Courier New", fontsize)	
	a = Font.render(text, False, color)
	return a

# list for rectangle objects, and color list
list = []
currentColor = ""

while running:	
        # mouse or touch position
	x,y = pygame.mouse.get_pos()
	mouse_pos = pygame.mouse.get_pos()				
	
	# random value for rgb colors	
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	pencolor = (r,g,b)
	
	# our rect object
	block =  (screen, pencolor,pygame.Rect((x-10), (y-10), 20, 20))	
	
	# list counter
	counter = len(list)
	
	# texts
	countText = addText(f"rect count : {counter}","#000000",30)
	colorText = addText(f"color : {currentColor}","#000000",30)
	mouse_posText = addText(f"x = {x} y = {y}", "#000000", 30)
	
	# for button
	btn_img = pygame.image.load("undo.png")
	btnScaled = pygame.transform.scale(btn_img, (200,100))
	btn = btnScaled.get_rect()	
	
	# checking for quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# function to check if user clicked surface
	def clicked():
		action = False
		if pygame.mouse.get_pressed()[0] == 1:
			action = True
		if pygame.mouse.get_pressed()[0] == 0:
			action = False
		return action
	
	# frame
	clock.tick(1000)
	
	# appending rectangle objects in list
	if clicked() and x >= 20 and y >= 120:
		list.append(block)
		currentColor = pencolor
	
	screen.blit(colorText, (30, 150))	
			
	# iterating list and displaying it one by one
	for i in list:
		pygame.draw.rect(i[0], i[1], i[2])
	
	# undo-ing
	if clicked() and btn.collidepoint(mouse_pos):
		if len(list) == 1:
			del list[0]
		elif len(list) > 1:
			del (list[-1])
			
	# displaying and updating game	
	pygame.display.update()
	pygame.display.flip()	
	screen.fill("#ffffff")
	screen.blit(btnScaled, (20,20))	
	screen.blit(countText, (30, 120))
	screen.blit(mouse_posText, (30, 180 ))
	
	# printing total boxes in screen after quiting
	print(f"total boxes : {len(list)}", end="\r")
pygame.quit()	
	
