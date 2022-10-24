#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame.display
import pygame.font
import pygame.time
import pygame.draw
import pygame.event
import pygame.surface
import subprocess
import math
from signal import pause
from gpiozero import Button
from songlist import *
from gpiozero import Button

#--- Initialization ----------------------------------------------------
PATH = "/home/k1t/soul/"
#PATH = "/home/sebi/m2i/soul/"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

pygame.display.init()
pygame.font.init()

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800,480))

#--- Clear current_value.txt -------------------------------------------
currentValue = ""
note = open(PATH + "current_value.txt", "w")
note.truncate()

done = False
clock = pygame.time.Clock()
startTimeCurrentChain = pygame.time.get_ticks()

#--- Initialise Idle-Animation -----------------------------------------
songOld = {}
song = Idle()
currentAnimationIndex = 0
#--- Get number of attached USB decvices--------------------------------
lsusb	= subprocess.Popen(["lsusb"],stdout=subprocess.PIPE)
devUSB = subprocess.Popen(['wc', '-l'],stdin=lsusb.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
lsusb.stdout.close()
numUSB = devUSB.stdout.read()
oldUSB = [int(i) for i in numUSB.split() if i.isdigit()][0]

#--- Initialise GPIO-Buttons -------------------------------------------
idlebutton 	= Button(2)
resetbutton = Button(3)
#--- Load images -------------------------------------------------------
animation_list = dict()

for sequence in sequence_list:

	animation_list[sequence] = {}
	
	for index in range(16):
	
		if sequence == 'AIRHORN' or sequence == 'SING5':	# for 16 unique images
			if index < 9:
				index_str = '0' +	str(index + 1)					
			else:
				index_str =			str(index + 1)		
		else:
			index_str = '0'+ str(math.floor(index/2) + 1)	# for  8 unique images

		animation_list[sequence][index] = pygame.image.load( PATH + 'img/' + sequence + '/' + sequence + '_0'	+ index_str + '.png' )	
		



