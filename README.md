# Modbus_test  Instructions
A small modbus communication project in ROS.   
Read data from USR-M100 and publish data in a loop as a node.  
This project is based on the pymodbus library，which is written in python.  
# Install pymodbus
The library is available on pypi.org and github.com to install with  
- `pip` for those who just want to use the library  
- `git` clone for those who wants to help or just are curious

Install with pip：  
&ensp;`pip install pymodbus`  
Install with github：  
&ensp;`git clone git://github.com/<your account>/pymodbus.git`  
&ensp;`cd pymodbus`  
&ensp;`python3 -m venv .venv`  
&ensp;`source .venv/bin/activate`  
# File Structure
.
├── LICENSE
├── README.md
├── scripts
│   ├── management_scripts
│   └── tools
└── src
    ├── ros_ht_msg
    └── ros_modbus_msg


