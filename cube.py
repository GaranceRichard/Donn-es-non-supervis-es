import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

sommets = (
	(1,-1,-1),	#0
	(1,1,-1),	#1
	(-1,1,-1),	#2
	(-1,-1,-1),	#3
	(1,-1,1),	#4
	(1,1,1),	#5
	(-1,1,1),	#6
	(-1,-1,1)	#7
	)

aretes = (
	(0,1),	#0
	(0,3),	#1
	(0,4),	#2
	(1,5),	#3
	(1,2),	#4
	(2,6),	#5
	(2,3),	#6
	(3,7),	#7
	(4,5),	#8
	(4,7),	#9
	(5,6),	#10
	(6,7),	#11
	)

faces = (
	(0,1,2,3),
	(0,1,5,4),
	(0,3,7,4),
	(6,2,1,5),
	(6,5,4,7),
	(6,2,3,7)
	)

colors = (
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(1,1,0),
	(1,0,1),
	(0,1,1),
	(0,1,0),
	(1,0,1),
	(0,1,1),
	(0,0,1)
	)

def Cube():
	glBegin(GL_QUADS)
	for face in faces:
		color = 0
		for vertex in face:
			color += 1
			glColor3fv(colors[color])
			glVertex3fv(sommets[vertex])
	glEnd()

	glBegin(GL_LINES)
	for arete in aretes:
		for vertex in arete:
			glVertex3fv(sommets[vertex])
	glEnd()

def main():
	pygame.init()
	display = (600,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	
	gluPerspective(45, (display[0]/display[1]), 6, 200.0)
	glTranslatef(0.0,0.0,-25)
	glRotatef(25,2,1,0)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1,0,0)
				if event.key == pygame.K_RIGHT:
					glTranslatef(1,0,0)
				if event.key == pygame.K_UP:
					glTranslatef(0,1,0)
				if event.key == pygame.K_DOWN:
					glTranslatef(0,-1,0)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1)
				if event.button == 5:
					glTranslatef(0,0,-1)


		#glRotatef(1,3,2,0)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)

main()