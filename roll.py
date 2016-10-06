#!/usr/bin/env python 
import random
import os, sys

if len(sys.argv) == 2:
	numb = 1
	sides = int(sys.argv[1])
	printall = False


if len (sys.argv) == 3:
	numb = int(sys.argv[1])
	sides = int(sys.argv[2])
	printall = False
	

if len(sys.argv) == 4:
	numb = int(sys.argv[1])
	sides = int(sys.argv[2])
	printall = True

def roll(numb, sides, printall):
	total = 0
	if numb == 1:
		total = random.randint(1,sides)
	else:
		for x in range(0,numb):
			value = random.randint(1,sides)
			if printall == True:
				print value
			total += value
	return total

print roll(numb, sides, printall)
