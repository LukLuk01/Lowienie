import threading
from scapy.all import *
from queue import Queue
import pyautogui
import pygetwindow as gw
import time
from WindowManager import WindowManager

class PacketSniffer:
    def __init__(self, interface, target_hex):
        self.interface = interface
        self.target_hex = target_hex
        self.data_queue = Queue()

    def packet_callback(self, packet):
        dst_port = None
        number = None
        if IP in packet and TCP in packet:
            raw_data = bytes(packet[TCP].payload)
            if self.target_hex in raw_data.hex():
                start_index = raw_data.find(b"jeszcze")+len(b"jeszcze ")
                number_bytes = raw_data[start_index:start_index + 1]
                dst_port = packet[TCP].dport
                number = int(number_bytes.decode('utf-8'))
                self.data_queue.put((dst_port, number))

    def start_sniffing(self):
        sniff(iface=self.interface, prn=self.packet_callback, filter="tcp and (dst port 55694 or dst port 55624) and src host 146.59.108.118")

class  BotInfo:
    def __init__(self,window_id,dst_port,space_press) -> None:
        self.window_id = window_id
        self.dst_port = dst_port
        self.space_press = space_press
        self.config = True
        self.fishing = False





if __name__ == "__main__":
    interface = "Ethernet"  # Zastąp "eth0" właściwą nazwą interfejsu Ethernet
    target_hex = "042b000e000000000208280"
    sniffer = PacketSniffer(interface, target_hex) #klasa przejmowania pakietow 

    window_title = "PolandMT2"  # Zastąp wartością tytułu okna, którą chcesz otworzyć
    window_manager = WindowManager(window_title) # obsluga okien

    objects = []
    windows_number = 1

    sniffer_thread = threading.Thread(target=sniffer.start_sniffing)
    sniffer_thread.daemon = True  # Ustawienie wątku jako demon powoduje zakończenie go, gdy główny wątek zakończy działanie
    sniffer_thread.start()
    
    # bot init conecting windows id with ports
    while windows_number > 0:
        if not sniffer.data_queue.empty():
            data = sniffer.data_queue.get()
            dst_port, number = data
            window_id = window_manager.get_active_window_id()
            bot_info = BotInfo(window_id, dst_port, number)
            objects.append(bot_info)
            windows_number = windows_number - 1

    # Główna pętla programu
    while True:
        if not sniffer.data_queue.empty():
            data = sniffer.data_queue.get()
            search_dst_port, number = data
            for obj in objects:
                if obj.dst_port == search_dst_port:
                    found_object = obj
                    break   
            #print("Otrzymano dane - dst_port:", dst_port, "number:", number)
            window_manager.click_window_by_id(found_object.window_id)
            window_manager.press_space_multiple_times(number)
            print('KOniec')
               
            # Tutaj możesz umieścić kod wykonujący operacje na danych
