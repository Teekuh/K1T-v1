#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'K1T v1.0 - Brought to life by Sev0r, AliasRoot & The_question'

import pygame.display
import pygame.font
import pygame.time
import pygame.draw
import pygame.event
import pygame.surface
from initalize import *
from K1T_functions import *
from songlist import *
from gpiozero import Button

#--- Main --------------------------------------------------------------
while not done:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(WHITE)
	
	devUSB = detect_usb()

	if devUSB > oldUSB:
		song = Insert_usb()
		oldUSB = devUSB
	if devUSB < oldUSB:
		song = Eject_usb()
		oldUSB = devUSB
	
	#--- Set back to IDLE if idlebutton is pressed ---------------------
	if(idlebutton.is_pressed):
		song = Idle()
		currentAnimationIndex = 0
		startTime = pygame.time.get_ticks()
	
	#------ Listen for Input -------------------------------------------
	note = open(PATH + "current_value.txt", "r")						
	lastValue = currentValue
	currentValue = note.read().strip()
	#-------------------------------------------------------------------
	
	if(currentValue != ''):	
		song = playSong(currentValue)		
			
	animate_returns = animate_song(screen, song, songOld, currentAnimationIndex, startTimeCurrentChain)
		
	song							= animate_returns[0]
	songOld						= animate_returns[1]
	currentAnimationIndex	= animate_returns[2]
	startTimeCurrentChain	= animate_returns[3]
	
			
