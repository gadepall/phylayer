#Code by GVV Sharma
#July 16, 2020
#Revised
#July 17, 2020
#Released under GNU/GPL
#Physical Layer Frame Parameters

BYTELEN= 8 # 1 byte = 8 bits
FrameDuration = 2e-3 #length of frame in seconds
BitDuration = 2.7e-6 #bit duration in seconds

#Time delays
RampTime = 116e-6 #ramp up time in secods
PropDelay = 100e-6 #Propagation delay


#SOM
SOMByte = 8 #Start of message in bytes
SOMBits = SOMByte*BYTELEN #Start of message in bytes
SOMDuration = SOMBits*BitDuration #SOM duration

#Pilot
PilotByte = 20.25 #Training sequence in bytes
PilotBits = PilotByte*BYTELEN #Training sequence in bytes
PilotDuration = PilotBits*BitDuration

#Payload
PayloadByte = 36 # Size of payload in bytes
PayloadBits = PayloadByte*BYTELEN # Size of payload in bytes
PayloadDuration = PayloadBits*BitDuration #Payload duration


#MAC overheads
MacOverheadDuration  =1092e-6-RampTime-SOMDuration -19.5*BYTELEN*BitDuration #MAC overhead duration
MacOverheadBits = MacOverheadDuration//BitDuration

#Verifying frame duration
print((FrameDuration-(RampTime+PropDelay+SOMDuration+PayloadDuration+MacOverheadDuration+PilotDuration))//BitDuration)
