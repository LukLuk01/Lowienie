import threading
from scapy.all import *
from queue import Queue
import pyautogui
import pygetwindow as gw
import time
from WindowManager import WindowManager
from BotInfo import BotInfo

class PacketSniffer:
    def __init__(self, interface, target_hex,fishing_end_info_unsucces,fising_end_info_succes):
        self.interface = interface
        self.target_hex = target_hex
        self.fishing_end_info_unsucces =fishing_end_info_unsucces
        self.fising_end_info_succes =fising_end_info_succes
        self.data_queue = Queue()
        self.fishing_info_queue = Queue()

    def packet_callback(self, packet):
        dst_port = None
        number = None
        state = False
        if IP in packet and TCP in packet:
            raw_data = bytes(packet[TCP].payload)
            if self.target_hex in raw_data.hex():
                start_index = raw_data.find(b"jeszcze")+len(b"jeszcze ")
                number_bytes = raw_data[start_index:start_index + 1]
                dst_port = packet[TCP].dport
                number = int(number_bytes.decode('utf-8'))
                self.data_queue.put((dst_port, number))
                print(f"---odebrano pakiet {dst_port}----\n")
            if self.fishing_end_info_unsucces in raw_data.hex():
                state = False
                dst_port = packet[TCP].dport
                self.fishing_info_queue.put((dst_port, state))
            if self.fising_end_info_succes in raw_data.hex():
                state = True
                dst_port = packet[TCP].dport
                self.fishing_info_queue.put((dst_port, state))


    def start_sniffing(self):
        sniff(iface=self.interface, prn=self.packet_callback, filter="tcp and (dst port 63226 or dst port 63499) and src host 146.59.108.118")


if __name__ == "__main__":

    interface = "Ethernet"  # Zastąp "eth0" właściwą nazwą interfejsu Ethernet
    target_hex = "042b000e000000000228"
    fishing_end_info_unsucces ="6e6965706f776f647a656e69656d2e"
    fising_end_info_succes = "20706f776f647a656e69656d2e5903f90d0000ffff"


    sniffer = PacketSniffer(interface, target_hex,fishing_end_info_unsucces,fising_end_info_succes) #klasa przejmowania pakietow 


    window_title = "PolandMT2"  # Zastąp wartością tytułu okna, którą chcesz otworzyć
    objects = [
        BotInfo(1377354, 63226, 0),
        BotInfo(197716, 63499, 0)
    ]    # bot init conecting windows id with ports

    window_manager = WindowManager(window_title,objects) # obsluga okien
    
    sniffer_thread = threading.Thread(target=sniffer.start_sniffing)
    sniffer_thread.daemon = True  # Ustawienie wątku jako demon powoduje zakończenie go, gdy główny wątek zakończy działanie
    sniffer_thread.start()
    #time.sleep(1)
    """
    windows_number = 2
    while windows_number > 0:
        if not sniffer.data_queue.empty():
            data = sniffer.data_queue.get()
            dst_port, number = data
            window_id = window_manager.get_active_window_id()
            bot_info = BotInfo(window_id, dst_port, number)
            objects.append(bot_info)
            windows_number = windows_number - 1

    """

    aktualny_czas = 0
    i=0
    # Główna pętla programu
    while True:
        if not sniffer.data_queue.empty():
            data = sniffer.data_queue.get()
            search_dst_port, number = data
            #print("Otrzymano dane - dst_port:", dst_port, "number:", number)
            window_manager.press_space_multiple_times(number,search_dst_port)
        
        for i in range(len(objects)):
            aktualny_czas = time.time()
            if( (aktualny_czas - objects[i].last_time_fishing_end > 10) and ( not sniffer.fishing_info_queue.empty() ) ):
                    data = sniffer.fishing_info_queue.get()
                    search_dst_port, state = data
                    window_manager.re_set(state, search_dst_port,objects[i])
        # Zaktualizuj indeks iteracji
        i = (i + 1) % len(objects)
