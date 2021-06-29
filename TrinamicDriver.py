#This is a script for controlling a Trinamic stepper motor using CANOpen protocol
#Using Kvaser canlib library

import time
import OpenCAN_CiA402 as op
from canlib import canlib, Frame


def ChannelParseData(channel):
    ch = canlib.ChannelData(channel)
    print("%d, %s,(%s / %s)" %(channel, ch.channel_name, ch.card_upc_no, ch.card_serial_no))


if __name__ == "__main__":

    print("Yeah it is comimg here")


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

    print("CAN bit rate",canlib.canBITRATE_1M)
    #ch1.busOff()

    ChannelParseData(channel1)
    ch1 = canlib.openChannel(channel1)
    ch1.setBusOutputControl(canlib.canDRIVER_NORMAL)
    ch1.setBusParams(canlib.canBITRATE_1M)   
    ch1.busOn()

    a = True

    while a:
        try:
            print("before")
            op.SendCANOpen(ch0)
            print("after")
            (msgId, msg, dlc, flg, time) = ch0.read()
            #frame = Frame(msgId, msg, flags=canlib.canMSG_EXT)
            #ch0.write(frame)
            print("Reply:",msgId, msg, dlc, flg, time)

            time.sleep(1)
        except:
            print("not able to send the messages")
            try:
                #frame = Frame(msgId+1, msg, flags=canlib.canMSG_EXT)
                ch1.write(frame)
            except:
                a = "Pani paali"
        a = False
