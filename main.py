import threading
from scapy.all import *
from queue import Queue
import time
from WindowManager import WindowManager
from BotInfo import BotInfo
from PacketSniffer import PacketSniffer


if __name__ == "__main__":

    mental = BotInfo(0)
    bufek = BotInfo(1)

    mental.skli_set('f1')    
    bufek.buff()

    #mental.check_conect_window_id_with_port()
    mental.add_task(150, mental.skli_set, 'f1')
    bufek.add_task(120,bufek.buff)
    mental.run()
    bufek.run()
    # Główna pętla programu
    while True:
        #mental.wait()
        for i in range(6):
            mental.press('4')
            mental.keydown('space')
            time.sleep(19)
            mental.swich_ch(i)
            bufek.swich_ch(i)

        


    