#This is a script for controlling a Trinamic stepper motor using CANOpen protocol
#Using Kvaser canlib library

import time
import OpenCAN_CiA402 as op

def ChannelParseData(channel):
    ch = canlib.ChannelData(channel)
    print("%d, %s,(%s / %s)" %(channel, ch.channel_name, ch.card_upc_no, ch.card_serial_no))


print("Yeah it is comimg here")
from canlib import canlib, Frame

channel = 0
channel1 = 1

#chd = canlib.ChannelData(channel)
num_channels = canlib.getNumberOfChannels()

print("No of channels: ",num_channels)

ChannelParseData(channel)
ch0 = canlib.openChannel(channel)
ch0.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch0.setBusParams(canlib.canBITRATE_1M)
ch0.busOn()
#ch1.busOff()

ChannelParseData(channel1)
ch1 = canlib.openChannel(channel1)
ch1.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch1.setBusParams(canlib.canBITRATE_1M)
ch1.busOn()

a = True

op.Print()

while a:
    try:
        (msgId, msg, dlc, flg, time) = ch0.read()
        #frame = Frame(msgId, msg, flags=canlib.canMSG_EXT)
        #ch0.write(frame)
        print(msgId, msg, dlc, flg, time)
        print("Coming here")
        time.sleep(1)
    except:
        print("not able to send the messages")
        try:
            #frame = Frame(msgId+1, msg, flags=canlib.canMSG_EXT)
            ch1.write(frame)
        except:
            a = "Pani paali"
    a = False
