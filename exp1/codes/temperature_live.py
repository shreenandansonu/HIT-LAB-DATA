import time  
# pip install pyserial
import serial 
import serial.tools.list_ports
# Get a list of available serial ports
available_ports = list(serial.tools.list_ports.comports())
# once obtaining available port
for port in available_ports:
    # we store the data into variable
    # baud rate should match the serial baudrate ie. 9600
    ard_data=serial.Serial(port.device,9600)
    # waiting 1 Sec for the communication to start
    time.sleep(1)
    while True:
        while(ard_data.inWaiting()==0):
            pass
        data=ard_data.readline()
        data=str(data,'utf-8')
        data=data.strip('\r\n')
        data=float(data)
        print(data)
