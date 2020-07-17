byte_len = 8 # 1 byte = 8 bits
frame_duration = 2e-3 #length of frame in seconds
bit_duration = 2.7e-6 #bit duration in seconds

#Time delays
t_ramp = 116e-6 #ramp up time in secods
t_prop_delay = 100e-6 #Propagation delay


#SOM
som_byte = 8 #Start of message in bytes
som_bits = som_byte*byte_len  #Start of message in bytes
t_som = som_bits*bit_duration #SOM duration

#Pilot
pilot_byte = 19.5 #Training sequence in bytes
pilot_bits = pilot_byte*byte_len #Training sequence in bytes
t_pilot = pilot_bits*bit_duration

#Payload
payload_byte = 32 # Size of payload in bytes
payload_bits = payload_byte*byte_len # Size of payload in bytes
t_payload = payload_bits*bit_duration #Payload duration


#MAC overheads
t_mac_overhead  =1092e-6-t_ramp-(som_bits+pilot_bits)*bit_duration #MAC overhead duration
mac_overhead_bits = t_mac_overhead//bit_duration

#Verifying frame duration
print((frame_duration-(t_ramp+t_prop_delay+t_som+t_payload+t_mac_overhead+t_pilot))//bit_duration)
