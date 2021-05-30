#This is a script for controlling a Trinamic stepper motor using CANOpen protocol
#Using Kvaser canlib library

from canlib import canlib, Frame

channel = 2
channel1 = 3

chd = canlib.ChannelData(channel)

ch0 = canlib.openChannel(channel, canlib.canOPEN_ACCEPT_VIRTUAL)
ch0.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch0.setBusParams(canlib.canBITRATE_1M)
ch0.busOn()
#ch1.busOff()


ch1 = canlib.openChannel(channel1, canlib.canOPEN_ACCEPT_VIRTUAL)
ch1.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch1.setBusParams(canlib.canBITRATE_1M)
ch1.busOn()

while True:
    try:
        (msgId, msg, dlc, flg, time) = ch0.read()
        #frame = Frame(msgId, msg, flags=canlib.canMSG_EXT)
        #ch0.write(frame)
        print(msgId, msg, dlc, flg, time)
    except:

        try:
            #frame = Frame(msgId+1, msg, flags=canlib.canMSG_EXT)
            ch1.write(frame)
        except:
            a = "Pani paali"
