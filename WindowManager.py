import pyautogui
import pygetwindow as gw
import time
import random
import keyboard
from pynput.keyboard import Key, Controller

class WindowManager:
    def __init__(self, window_title):
        self.window_title = window_title

    def bring_window_to_front(self, index=0):
        windows = gw.getWindowsWithTitle(self.window_title)
        if windows and index < len(windows):
            window = windows[index]
            left, top, right, _ = window.left, window.top, window.right, window.top + 30  # 30 pikseli na wysokość paska tytułowego
            center_x = left + (right - left) // 2
            center_y = top + 15  # Środek paska tytułowego
            pyautogui.moveTo(center_x, center_y, duration=0.5)
            pyautogui.click()
        else:
            print(f"Nie znaleziono okna o tytule '{self.window_title}' o indeksie {index}.")

    def click_window_by_id(self, window_id):
        windows = gw.getWindowsWithTitle(self.window_title)
        for window in windows:
            if window._hWnd == window_id:
                left, top, right, _ = window.left, window.top, window.right, window.top + 30  # 30 pikseli na wysokość paska tytułowego
                center_x = left + (right - left) // 2
                center_y = top + 15  # Środek paska tytułowego
                pyautogui.moveTo(center_x, center_y+30, duration=0.5)
                pyautogui.leftClick()
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

    def press_space_multiple_times(self,num_times):
        keyboard = Controller()
        time.sleep(random.uniform(0.1 , 0.3))
        for _ in range(num_times):
            print("klik")
            keyboard.press(Key.space)
            time.sleep(random.uniform(0.2 , 0.3))
            keyboard.release(Key.space)
            time.sleep(random.uniform(0.3, 0.7))  # Zwiększono zakres opóźnienia
            #pyautogui.press('space')
            #keyboard.press_and_release('space')
            #time.sleep(random.uniform(0.1 , 0.15))
