#! /usr/bin/env python

import rospy
from pymodbus.client.tcp import ModbusTcpClient
from connect_tcp.msg import pub

class JMModbusClient():
    """Class object for modbus communication
    :param host:Host IP address of the modbus server
    :param port: (optional) Port used for communication
    """
    def __init__(self,host:str,port:int=502):
        """Create a client object"""
        self.client = ModbusTcpClient(host,port)
    
    def jmconnect(self):
        """Try connecting to the server"""
        self.client.connect()
    
    def jmclose(self):
        """Close Connection"""
        self.client.close()
    
    def Read_device(self,slaveid:int,device_name:str,start_address:int=0,num:int=4):
        """Read the holding registers
        :param slaveid:Modbus server slave ID
        :param device_name:The name of Modbus server or data set
        :param start_address:(optional) Start address of the registers to read from
        :param num:(optional) Number of registers to read
        """
        # Read the holding registers ,the return value is a class ,value stored in .registers list
        response = self.client.read_holding_registers(address=start_address,count=num,slave=slaveid)
        result = response.registers
        # Save values in the class pub 
        msg = pub()
        msg.name = device_name
        msg.data01 = result[0]
        msg.data02 = result[1]
        msg.data03 = result[2]
        msg.data04 = result[3]
        return msg
        
    

    

    






        
    
