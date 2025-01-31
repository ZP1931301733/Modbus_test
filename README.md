# Ros_modbus_test Package Instructions
A small modbus communication test package in ROS.

Read data from USR-M100 and publish data in a loop as a node.

This package is based on the pymodbus library，which is written in python.

[pymodbus](https://github.com/pymodbus-dev/pymodbus)
# Install pymodbus
The library is available on pypi.org and github.com to install with  
- `pip` for those who just want to use the library  
- `git` clone for those who wants to help or just are curious

Install with pip：  
  ```bash
  pip install pymodbus
  ```
Install with github:  
  ```bash
  git clone git://github.com/pymodbus-dev/pymodbus.git
  cd pymodbus
  python3 -m venv .venv
  source .venv/bin/activate
  ```
To get a specific release:
 ```bash
  git checkout v3.5.2
  ```
# File Structure
  ```
  .
  ├──doc
  ├──msg
  │   ├──pub.msg
  ├──scripts
  │   ├──test.py
  ├──src
  │   ├──Modbus_test
  ```
Here the function of these files：
- `doc` contains the specifications and test results.
- `msg` contains the self-defined data types.
- `scripts` contains the node program files.
- `src` contains the engineering functional modules.
    

    


