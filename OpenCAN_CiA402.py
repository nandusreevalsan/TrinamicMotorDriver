#This file contains functions for CiA402 protocols

from canlib import canlib, Frame

def Print():
    print("Nammuku ingane okke pattum ketto, eethu")

def Concatenate(data7,data6,data5,data4,data3,data2,data1,data0):
    data = data7<<(7*8)|data6<<(6*8)|data5<<(5*8)|data4<<(4*8)|data3<<(3*8)|data2<<(2*8)|data1<<(1*8)|data0
    return data

def SendCANOpen(channel):
    data7 = 0x40
    data6 = 0x18
    data5 = 0x10
    data4 = 0x01
    data3 = 0x00
    data2 = 0x00
    data1 = 0x00
    data0 = 0x00

    Data = [data7,data6,data5,data4,data3,data2,data1,data0]
    print("Data:",Data)
    frame = Frame(id_= 0x601,data = Data ,dlc=8)
    print(frame)
    channel.write(frame)
    print("After write")
