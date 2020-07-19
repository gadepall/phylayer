#Code by GVV Sharma
#July 10, 2020
#Revised
#July 13, 2020
#Revised
#July 17, 2020
#Released under GNU/GPL
#SER and BER simulation for 8-PSK 
#using complex symbols

import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

#Importing custom functions
from EightPSK.mod import *
from EightPSK.demod import *
from EightPSK.mats import *
from frame.frametx import *
from frame.FrameParams import *

#print(len(TotBits))

#print(20*(PilotBits+SOMBits+PayloadBits))
#print(PilotBits)
#print(nFrame*PilotBits,nFrame*PayloadBits)
#print(FramePilot)
#print(FrameSOM)
#print(len(bits))
#print(PayloadBitsLen)
#print(SOMBitsLen, len(SOMBits))
#print(PilotBitsLen, len(PilotBits))
#print(len(PilotBits))
#FrameMAC = FrameMACGen(0) 
#print(FrameMAC)
#print(len(FrameMAC))

#print(MACBitsLen)
#print(PilotBitsLen)
#print(len(FrameGen(1)),SOMBitsLen+PilotBitsLen+MACBitsLen+PayloadBitsLen)
#print(FrameGen(1))
