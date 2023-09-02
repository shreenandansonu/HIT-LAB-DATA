import time
import serial
import pandas as pd
import numpy as np
import serial.tools.list_ports
name=input("Name of the Patient:- ")
# Get a list of available serial ports
available_ports = list(serial.tools.list_ports.comports())
#initializing a numpy array to store 10000 temperature data points
data_array=np.zeros(10000)
t=0
# begins the counter
t1=time.time()
# once obtaining available port
for port in available_ports:
    # we store the data into variable
    # baud rate should match the serial baudrate ie. 9600
    ard_data=serial.Serial(port.device,9600)
    time.sleep(1)
    #seting the loop for 10000 times
    while t<10000:
        while(ard_data.inWaiting()==0):
            pass
        #processing the data from serial port and converting it to integer
        data=ard_data.readline()
        data=str(data,'utf-8')
        data=data.strip('\r\n')
        data=int(data)
        print(data)
        data_array[t]=data
        t=t+1
    # ending the counter
    t2=time.time()
    print(t2-t1)    
    print("Collected")
    print(data_array)
    # making a data frame to hold the numpy data
    df = pd.DataFrame(data_array)
    # converting the dataframe to csv file
    df.to_csv(name +'.csv')
    print('Thank You')