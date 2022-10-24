#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--- Define image series -----------------------------------------------
sequence_list = [	'IDLE', 'AIRHORN', 'BLINK', 'BLUSH', 'EMO', 'EVIL', 
						'EVILLOL', 'FIRE', 'HAPPY', 'HEADBANG', 'HEHE', 
						'LISTEN', 'LOVE', 'NOTE', 'OLD1', 'OLD2', 'OLD3', 
						'POMMES', 'SING1', 'SING2', 'SING3', 'SING4', 'SING5', 
						'SURPRISED', 'VILLAIN', 'WINK' ]				
						
#--- Song-Sequences ----------------------------------------------------
def Idle():
	bpm 				= 120
	sequence 		= ["IDLE"]
	sequenceTime 	= [15]
	return (bpm, sequence, sequenceTime)
#-----------------------------------------------------------------------
def Idle_animation():
	bpm 				= 240
	sequence 		= ["IDLE","IDLE","IDLE","IDLE","IDLE","IDLE","IDLE","IDLE"]
	sequenceTime 	= [11, 11, 11, 11, 11, 11, 11, 11]
	return (bpm, sequence, sequenceTime)
#-----------------------------------------------------------------------
def Airhorn():
	bpm 				= 160
	sequence 		= ["AIRHORN"]
	sequenceTime 	= [15]
	return (bpm, sequence, sequenceTime)
#-----------------------------------------------------------------------
def Insert_usb():
	bpm 				= 160
	sequence 		= ["LOVE"]
	sequenceTime 	= [15]
	return (bpm, sequence, sequenceTime)
#-----------------------------------------------------------------------
def Eject_usb():
	bpm 				= 160
	sequence 		= ["BLUSH"]
	sequenceTime 	= [15]
	return (bpm, sequence, sequenceTime)	
#-----------------------------------------------------------------------	
def Chronos():
	#F2 - Chronos - 123BPM - 151 bars (2 Prebars)
	bpm = 123
	sequence = ["VILLAIN","VILLAIN", 															#2 Bars, Pre-Count
	"HEADBANG", "HEADBANG","HEADBANG","HEADBANG", 												#4 Bars Intro
	"VILLAIN","VILLAIN","VILLAIN","VILLAIN", "VILLAIN","VILLAIN","VILLAIN","VILLAIN", 			#8 Bars First Verse, first half
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1", 							#8 Bars First Verse, second half
	"VILLAIN","VILLAIN",																		#2 Bars PreChorus
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1",							#8 Bars Chorus, first half
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1",							#8 Bars Chorus, second half
	"SING1","VILLAIN","SING1",																	#3 Bars PostChorus
	"VILLAIN","VILLAIN","VILLAIN","VILLAIN","VILLAIN","VILLAIN","VILLAIN","VILLAIN",			#8 Bars Second Verse, first half
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1",							#8 Bars Second Verse, second half
	"HEADBANG","HEADBANG",																		#2 Bars PreChorus
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1",							#8 Bars Chorus, first half
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1",							#8 Bars Chorus, second half
	"LISTEN","NOTE","LISTEN","NOTE","LISTEN","NOTE","LISTEN","NOTE",							#8 Bars Melodic Solo, first half
	"LISTEN","NOTE","LISTEN","NOTE","LISTEN","NOTE","LISTEN","NOTE",							#8 Bars Melodic Solo, second half
	"HEADBANG","NOTE","HEADBANG","NOTE","HEADBANG","NOTE","HEADBANG","NOTE",					#8 Bars Dubstep-Part
	"EVIL","EVIL","EVIL","EVIL","EVIL","EVIL","EVIL","EVIL",									#8 Bars Guitar Solo, first half
	"EVIL","EVIL",																				#2 Bars Clock
	"EVILLOL","EVILLOL","EVILLOL","HEADBANG","SING1","SING1","SING1","SING2",					#8 Bars Last Chorus, first half
	"SING1","SING1","SING1","SING1","SING1","SING1","SING1","SING1",							#8 Bars Last Chorus, second half
	"SING1","NOTE","NOTE","NOTE","NOTE","NOTE","NOTE","NOTE",									#24 Bars 8-Bit Outro
	"NOTE","NOTE","NOTE","NOTE","NOTE","NOTE","NOTE","NOTE",
	"NOTE","NOTE","NOTE","NOTE","NOTE","NOTE","NOTE","NOTE"]
	
	sequenceTime = [15]*len(sequence)
	
#	sequenceTime = [15, 15, 
#	15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15,
#	15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15,
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15, 
#	15, 15, 15, 15, 15, 15, 15, 15]
	return(bpm, sequence, sequenceTime)
#-----------------------------------------------------------------------		

#--- Define keyvalues for songs ----------------------------------------
song_list = { '41' : Chronos, '42' : Idle_animation, '69' : Airhorn, '420' : Insert_usb, '421' : Eject_usb }
