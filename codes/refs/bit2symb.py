#Code by GVV Sharma
#July 9, 2020
#Released under GNU/GPL
#Converts bitstream to 8-PSK symbol stream
import numpy as np
from bs import bitstream
from mapping_new import mapping

def symb(bits):
	symbol =[]
	i = 0
	while(1):
		try:
			symbol.append(mapping(bits[i],bits[i+1],bits[i+2]))
			i = i+3
		except IndexError:
			return symbol

