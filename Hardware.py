'''Hardware modules definitions will be here'''

import os
import glob
import socket
import csv

class Node():
    id= 0
    def __init__(self, name, ip_address, mac_address, access_key, comment=""):
        self.id +=1
        self.name = name
        self.ip = ip_address
        self.mac = mac_address
        self.key = access_key
        self.comment = comment
    
    def Send_Data(receiver_ip, data):
        pass

    def Receive_Data():
        pass
    
    def Get_Online():
        pass

class Remote_IO(Node):
    def __init__(self, name, ip_address, mac_address, access_key, , comment=""):
        super().__init__(name, ip_address, mac_address, access_key, comment)

class CPU(Node):
    pass

class Analog_Input():
    pass

class Analog_Output():
    pass

class Digital_Input():
    pass

class Digital_Output():
    pass

class Definition():
    pass