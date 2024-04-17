
from WindowManager import WindowManager
from PacketSniffer import PacketSniffer
import pydirectinput
import random
import sched
import time
import threading

class  BotInfo:
    def __init__(self,bot_num) -> None:
            
        window_title = "PolandMT2"  # Zastąp wartością tytułu okna, którą chcesz otworzyć
        interface = "Ethernet"  # Zastąp "eth0" właściwą nazwą interfejsu Ethernet
        target_ip = "146.59.108.118"
        target_hex = None # informacja do snifera 
        
        #self.sniffer = PacketSniffer(interface, target_ip, target_hex ) #klasa przejmowania pakietow 
        #ports = self.sniffer.check_tcp_ports()
        #self.dst_port=ports

        self.window_manager = WindowManager(window_title) # obsluga okien
        windows_id = self.window_manager.find_window_id()
        self.window_id = windows_id[bot_num]

        #           -sheduler-
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.pause_event = threading.Event()

        #--------------ZMIENNNE---------------   
        self.last_time = time.time()
        self.now_time = time.time()
        self.config = True

        self.skli_status = None
        self.on_hors = False
        self.focus =False

        #key map
        NUM1 = 'numpad1'
        NUM2 = 'numpad2'
        NUM3 = 'numpad3'
        NUM4 = 'numpad4'
        NUM5 = 'numpad5'
        NUM6 = 'numpad6'
        pydirectinput.KEYBOARD_MAPPING[NUM1] = 0x4F
        pydirectinput.KEYBOARD_MAPPING[NUM2] = 0x50
        pydirectinput.KEYBOARD_MAPPING[NUM3] = 0x51
        pydirectinput.KEYBOARD_MAPPING[NUM4] = 0x4B
        pydirectinput.KEYBOARD_MAPPING[NUM5] = 0x4C
        pydirectinput.KEYBOARD_MAPPING[NUM6] = 0x4D

    def check_conect_window_id_with_port(self):
        self.window_manager.click_window_by_id(self.window_id)
        pydirectinput.typewrite('f1')
        while not seting:
            user_input = input("Naciśnij Enter, aby zakończyć: ")
            if user_input == "":
                seting = True
            else:
                print("zamiana okna ...")
                windows_id = self.window_manager.find_window_id()
                self.window_id = windows_id[1]
                return False

    def press(self,key):
        self.window_manager.activate_window_by_id(self.window_id)
        
        pydirectinput.keyDown(key)
        time.sleep(random.uniform(0.061 , 0.085 ))
        pydirectinput.keyUp(key)
    
    def get_on_mount(self):
        self.window_manager.activate_window_by_id(self.window_id)    

        pydirectinput.keyDown('g')
        time.sleep(random.uniform(0.061 , 0.085 ))
        pydirectinput.keyUp('g')
        self.on_hors = not self.on_hors

    def bost_set(self):
        self.window_manager.activate_window_by_id(self.window_id)  

        self.press('numpad8')

    def skli_set(self,key):
        self.window_manager.activate_window_by_id(self.window_id)  

        if(self.on_hors == True):
            self.get_on_mount()
            time.sleep(random.uniform(0.161 , 0.285 ))
    
        self.press(key)

        if(self.on_hors == False):
            time.sleep(random.uniform(0.161 , 0.285 ))
            self.get_on_mount()

    def add_task(self, interval, func, *args, **kwargs):
        def wrapper():
            func(*args, **kwargs)
            self.pause_event.set()  # Zresetuj flagę pause_event po wykonaniu zadania
            self.scheduler.enter(interval, 1, wrapper)
        self.scheduler.enter(interval, 1, wrapper)

    def run(self):
        threading.Thread(target=self._scheduler_thread).start() 
    
    def _scheduler_thread(self):
        while True:
            self.scheduler.run()
            self.pause_event.clear()  # Zresetuj flagę pause_event po wykonaniu wszystkich zadań

    def wait(self):
        self.pause_event.wait()

    def buff(self):
        self.window_manager.activate_window_by_id(self.window_id)
        self.window_manager.click_on_pt_partner(self.window_id)  
        self.press('f1')
        time.sleep(random.uniform(2 , 2.2 ))
        self.press('f2')
        time.sleep(random.uniform(2 , 2.2 ))
        self.press('f3')

    def swich_ch(self,ch):
        self.window_manager.activate_window_by_id(self.window_id)  
        if(ch==1):
            self.press('numpad1')
            time.sleep(5)
        elif(ch==2):
            self.press('numpad2')
            time.sleep(5)
        elif(ch==3):
            self.press('numpad3')
            time.sleep(5)
        elif(ch==4):
            self.press('numpad4')
            time.sleep(8)
        elif(ch==5):
            self.press('numpad5')
            time.sleep(5)
        elif(ch==6):
            self.press('numpad6')
            time.sleep(5)

    def keydown(self,key):
        self.window_manager.activate_window_by_id(self.window_id)  
        pydirectinput.keyDown(key)
