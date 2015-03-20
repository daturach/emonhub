#!/usr/bin/python
#Script to test emoncms.org without any hardware, just a raspi connected to internet
#To use the below script, you have to add the below lines to emonhub.conf in the [Interfacer] section
#Note that the port number must match!
#[[Socket]]   # Any unique name
#    Type = EmonHubSocketInterfacer
#    [[[init_settings]]]
#        port_nb = 50011
#    [[[runtimesettings]]] 

import socket
import random
#########
# Frame #
#########
# Script that results in a "frame" string starting with a node id followed by val1 val2 etc 
#frame = "10 1 2 3 4"
power = str(round(1000 *random.random(),0))
solar_power = str(round(1000 *random.random(),0))

#pompe a chaleur
heatpump_power = str(random.randrange(5000, 10000, 1))
#heatpump_kwh =  This will be a calculated feed
heatpump_flow_temp = str(random.randrange(35, 50, 1))
heatpump_return_temp = str(random.randrange(18, 22, 1))
ambient_temp = str(random.randrange(10, 15, 1))
room_temp = str(random.randrange(19, 24, 1))

frame = "10 " +  power + " 240 15 23 " + solar_power + " 1300 295 89 " + heatpump_power + " " + heatpump_flow_temp + " " + heatpump_return_temp + " " + ambient_temp + " " + room_temp
#frame = "10 " +  power + " 240 15 23 " + solar_power + " 1300 295 89 " + heatpump_power + " " + heatpump_flow_temp
#print (frame)
# 
##############
# Parameters #
##############
# HOST: hostname or IP address of emonHub
HOST = 'localhost'
# PORT: port number to the emonHub interfacer
PORT = 50011
########
# Code #
########
# Append line ending
frame = frame + '\r\n'
# Send frame of data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(frame)
s.close()

