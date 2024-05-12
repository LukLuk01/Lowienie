import threading
from scapy.all import *
from queue import Queue
import time
from WindowManager import WindowManager
from BotInfo import BotInfo
from PacketSniffer import PacketSniffer


def init(objects):
        for obj  in objects:
            window_manager.re_set(obj)
            setuping = True
            while(setuping==True):
                if not sniffer.data_queue.empty():
                    data = sniffer.data_queue.get()     
                    search_dst_port, number = data
                    obj.dst_port = search_dst_port
                    window_manager.press_space_multiple_times(number,search_dst_port)
                    setuping = False


if __name__ == "__main__":

    interface = "Ethernet"  # Zastąp "eth0" właściwą nazwą interfejsu Ethernet
    target_hex = "042b000e0000000002a" # informacja o ilosc spacji
    
    fishing_end_info_unsucces ="6e6965706f776f647a656e69656d2e" # informacja o  nie pomysllnym p olowie
    fising_end_info_succes = "20706f776f647a656e69656d2e5903f90d0000ffff" # informacja o pomysllnym polowie
    target_ip = "146.59.108.118"

    window_title = "PolandMT2"  # Zastąp wartością tytułu okna, którą chcesz otworzyć
    objects = [] 

    sniffer = PacketSniffer(interface, target_ip,target_hex,fishing_end_info_unsucces,fising_end_info_succes) #klasa przejmowania pakietow 
    #time.sleep(1)
    game_ports = sniffer.check_tcp_ports()

    for port in game_ports:
        objects.append(BotInfo(0,0,0))

    window_manager = WindowManager(window_title, objects) # obsluga okien
    window_manager.find_window_id()
    
    #time.sleep(1)
   # bot init conecting windows id with ports
    sniffer_thread = threading.Thread(target=sniffer.start_sniffing)
    sniffer_thread.daemon = True  # Ustawienie wątku jako demon powoduje zakończenie go, gdy główny wątek zakończy działanie
    sniffer_thread.start()

    init(objects) 
    time.sleep(1)
    window_manager.start_scheduler()

    # Główna pętla programu
    while True:
        if not sniffer.data_queue.empty():
            data = sniffer.data_queue.get()
            search_dst_port, number = data
            window_manager.press_space_multiple_times(number,search_dst_port)
        aktualny_czas = time.time()
        for obj in objects:  
            if( (aktualny_czas - obj.last_time_fishing_end > (random.uniform( 9, 9.4)) and obj.fishing == False or aktualny_czas- obj.last_trow > 20)):
                window_manager.re_set(obj)
        


