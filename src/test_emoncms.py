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
#########
# Frame #
#########
# Script that results in a "frame" string starting with a node id followed by val1 val2 etc 
#frame = "10 1 2 3 4"
frame = "10 1290.0 240 15 23 1200 1300 295 89"
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
