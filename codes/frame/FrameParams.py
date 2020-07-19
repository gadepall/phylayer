#Code by GVV Sharma
#July 16, 2020
#Revised
#July 17, 2020
#Released under GNU/GPL
#Physical Layer Frame Parameters

from  EightPSK.mod import bitstream


nFrame =  62
BYTELEN= 8 # 1 byte = 8 bits
FrameDuration = 2e-3 #length of frame in seconds
BitDuration = 2.7e-6 #bit duration in seconds
#Time delays
RampTime = 116e-6 #ramp up time in secods
PropDelay = 100e-6 #Propagation delay


#SOM
SOMByte = 8 #Start of message in bytes
SOMBitsLen = int(SOMByte*BYTELEN) #Start of message in bytes
SOMDuration = SOMBitsLen*BitDuration #SOM duration
SOMBits = bitstream(SOMBitsLen)

#Pilot
PilotByte = 20.25 #Training sequence in bytes
PilotBitsLen = int(PilotByte*BYTELEN) #Training sequence in bytes
PilotDuration = PilotBitsLen*BitDuration
PilotBits = bitstream(PilotBitsLen)

#Payload
PayloadByte = 36 # Size of payload in bytes
PayloadBitsLen = int(PayloadByte*BYTELEN) # Size of payload in bytes
PayloadDuration = PayloadBitsLen*BitDuration #Payload duration


#MAC 
MACDuration  =1092e-6-RampTime-SOMDuration -19.5*BYTELEN*BitDuration #MAC  duration
MACBitsLen = int(MACDuration//BitDuration)

#Verifying frame duration
#print((FrameDuration-(RampTime+PropDelay+SOMDuration+PayloadDuration+MACDuration+PilotDuration))//BitDuration)

FrameLen = SOMBitsLen+PilotBitsLen+MACBitsLen+PayloadBitsLen
TotBits = bitstream(nFrame*PayloadBitsLen)
