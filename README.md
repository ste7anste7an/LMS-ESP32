# LMS-ESP32 Drivers and Software
In this repository you will fid all drivers and software needed to operate your LMS-ESP32 and LMS-ESP32v2.

Based on the hub you are using, choose the appropriate directories. here you will find files you need to instal on the hub and pointers to the firmware that needs to be instaled on the LMS-ESP32 module.

We discern the following types of Lego hubs:
- SPIKE3: This is the newest SPIKE Education software running on the yellow SPIKE and SPIKE Essential hubs
- SPIKE2: This is the Legacy SPIKE software wich seems to be supported unitl end of 2023
- Inventor: This is the legacy Mindstorms Robot Inventor software which runs on the blue inventor hub
- PyBricks: This is the alternative firmware that runs on almost any Lego hub
 
|Mode of operation | Lego hub config | Firmware on LMS-ESP32 | 
|------------------|-----------------------|-----------------|
|BluePad32         | SPIKE3 | BluePad32 for Spike3 and Pybricks |
|BluePad32         | PyBricks | BluePad32 for Spike3 and Pybricks | 
|PUPRemote         | PyBricks | MicroPython v1.24 uartremote+pupremote | 
| UARTRemote or SerialTalk | SPIKE2 or Inventor |MicroPython v1.24 uartremote+pupremote | 


## PyBricks

## SPIKE Education aka SPIKE3

## Legacy Spike and legacy Mindstorms Inventor
