import pyautogui
import pygetwindow as gw
import time
import random
from pynput.keyboard import Key, Controller
import pydirectinput
import threading
import sched

class WindowManager:
    def __init__(self, window_title, bots_objects):
        self.window_title = window_title
        self.bots_objects = bots_objects
        self.delay_press=1815
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def find_window_id(self):
        window = gw.getWindowsWithTitle(self.window_title)
        if window:
            print(f"Znaleziono okno o nazwie '{self.window_title}':")
            for i, w in enumerate(window):
                print(f"Identyfikator: {w._hWnd}, Indeks: {i}")
                self.bots_objects[i].window_id = w._hWnd
        else:
            print(f"Nie znaleziono okna o nazwie '{self.window_title}'.")

    def click_window_by_id(self, window_id):
        windows = gw.getWindowsWithTitle(self.window_title)
        for window in windows:
            if window._hWnd == window_id:
                left, top, right, _ = window.left, window.top, window.right, window.top + 30  # 30 pikseli na wysokość paska tytułowego
                center_x = left + (right - left) // 2
                center_y = top + 15  # Środek paska tytułowego
                pyautogui.moveTo(center_x, center_y+20, duration=0.5)
                pyautogui.rightClick()
                return
        print(f"Nie znaleziono okna o identyfikatorze '{window_id}'.")


    def get_active_window_id(self):
        active_window = gw.getActiveWindow()
        if active_window:
            active_window_id = active_window._hWnd
            print("Aktualnie aktywne okno to:", active_window.title)
            print("ID tego okna:", active_window_id)
            return active_window_id
        else:
            return None

    def press_space_multiple_times(self,num_times,search_dst_port):
        print('----wyciaganie----')
        for obj in self.bots_objects: 
            if obj.dst_port == search_dst_port:
                    found_object = obj
                    break   
            
        keyboard = Controller()
        self.click_window_by_id(found_object.window_id)
        for _ in range(num_times):
            keyboard.press(Key.space) 
            time.sleep(random.uniform(0.1,0.3 ))  # Zwiększono zakres opóźnienia
            keyboard.release(Key.space)
            time.sleep(random.uniform(0.1, 0.3))  # Zwiększono zakres opóźnienia
        #print('---Zakonczono wyciaganie----')
        found_object.last_time_fishing_end = time.time()
        found_object.fishing = False

    def re_set(self,bot):
        self.click_window_by_id(bot.window_id)

        time.sleep(random.uniform(0.2 , 0.3 ))  # Zwiększono zakres opóźnienia
        pydirectinput.typewrite('1')
        time.sleep(random.uniform(0.2 , 0.3 ))  # Zwiększono zakres opóźnienia
        # Wciskanie spacji
        pydirectinput.typewrite(' ')

        print(" ----zarzucono---- ")
        bot.fishing = True
        bot.last_trow = time.time()
    
    def start_scheduler(self):
        self.scheduler.enter( self.delay_press, 1, self.add_5_prc_bonus, ())  # Rozpocznij wykonywanie funkcji press_key_2 co 30 minut
        scheduler_thread = threading.Thread(target=self.scheduler.run)
        scheduler_thread.daemon = True
        scheduler_thread.start()

    def add_5_prc_bonus(self):
        print("dodano 5 proc 1bonusus")
        for obj in self.bots_objects:
            self.click_window_by_id(obj.d)
            pydirectinput.typewrite('2')
        self.scheduler.enter( self.delay_press, 1, self.add_5_prc_bonus, ())  # Zaplanuj kolejne naciśnięcie klawisza "2" za 30 minut
