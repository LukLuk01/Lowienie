import pyautogui
import pygetwindow as gw
import time
def bring_window_to_front(window_title, index=0):
    windows = gw.getWindowsWithTitle(window_title)
    if windows and index < len(windows):
        window = windows[index]
        left, top, right, _ = window.left, window.top, window.right, window.top + 30  # 30 pikseli na wysokość paska tytułowego
        center_x = left + (right - left) // 2
        center_y = top + 15  # Środek paska tytułowego
        pyautogui.moveTo(center_x, center_y, duration=0.5)
        pyautogui.click()
    else:
        print(f"Nie znaleziono okna o tytule '{window_title}' o indeksie {index}.")

def get_active_window():
    active_window = gw.getActiveWindow()
    if active_window:
        active_window_id = active_window._hWnd
        print("Aktualnie aktywne okno to:", active_window.title)
        print("ID tego okna:", active_window_id)
    else:
        print("Brak aktywnego okna.")


if __name__ == "__main__":
    window_title = "PolandMT2"  # Zastąp wartością tytułu okna, którą chcesz otworzyć
    index = 1  # Indeks okna do wyboru (liczone od zera)
    #bring_window_to_front(window_title, index)
    time.sleep(3)
    get_active_window()
