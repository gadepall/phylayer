#Code by GVV Sharma
#July 17, 2020
#Released under GNU/GPL
#Frame genration at transmitter

from EightPSK.mats import *
from EightPSK.mod import bitstream
from . FrameParams import *

#Generating Payload for the frame
def FramePayloadGen(FrameNo):
	return TotBits[PayloadBitsLen*FrameNo:(PayloadBitsLen*(FrameNo+1))]

#Generating MAC
def FrameMACGen(FrameNo):
	return bitstream(MACBitsLen)

#Generating Frame given the frame no
def FrameGen(FrameNo):
	FramePayload = FramePayloadGen(FrameNo) 
	FrameMAC = FrameMACGen(FrameNo) 
	Frame =np.hstack((SOMBits,PilotBits,FrameMAC,FramePayload)) 	
	return Frame

