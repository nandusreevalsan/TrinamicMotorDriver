#This is a script for controlling a Trinamic stepper motor using CANOpen protocol
#Using Kvaser canlib library
print("Yeah it is comimg here")
from canlib import canlib, Frame

channel = 1
channel1 = 2

chd = canlib.ChannelData(channel)
num_channels = canlib.getNumberOfChannels()

print("No of channels: ",num_channels)
ch0 = canlib.openChannel(channel, canlib.canOPEN_ACCEPT_VIRTUAL)
ch0.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch0.setBusParams(canlib.canBITRATE_100K)
ch0.busOn()
#ch1.busOff()


ch1 = canlib.openChannel(channel1, canlib.canOPEN_ACCEPT_VIRTUAL)
ch1.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch1.setBusParams(canlib.canBITRATE_100K)
ch1.busOn()

while True:
    try:
        (msgId, msg, dlc, flg, time) = ch0.read()
        #frame = Frame(msgId, msg, flags=canlib.canMSG_EXT)
        #ch0.write(frame)
        print(msgId, msg, dlc, flg, time)
        print("Coming here")
    except:

        try:
            #frame = Frame(msgId+1, msg, flags=canlib.canMSG_EXT)
            ch1.write(frame)
        except:
            a = "Pani paali"
