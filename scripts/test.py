#! /usr/bin/env python
"""
   Establish a modbus connection and cyclically publish the data read from the holding registers
"""
import rospy
from Modbus_test.JMModbusClient import JMModbusClient
from connect_tcp.msg import pub



if __name__=="__main__":
    rospy.init_node("modbus_client")

    host = "192.168.0.7"
    port = 502

    client = JMModbusClient(host,port)
    client.jmconnect()
    # Create publisher object
    pub_data = rospy.Publisher("JM",pub,queue_size=20)
    rate = rospy.Rate(1)
    # Send data every second in a loop
    while not rospy.is_shutdown():
        msg1 = client.Read_device(slaveid=1,device_name="device01")
        
        # msg2 = client.Read_device(slaveid=2,device_name="device02")
        rospy.loginfo("Data is updated")
        rospy.loginfo("\n name:%s \n data01:%d \n data02:%d \n data03:%d \n data04:%d \n",msg1.name,msg1.data01,msg1.data02,msg1.data03,msg1.data04)
        pub_data.publish(msg1)
        # publisher.publish(msg2)
        rate.sleep()
    

    