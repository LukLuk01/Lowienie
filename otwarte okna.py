import pygetwindow as gw
import win32gui
import time
def find_window_id(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        print(f"Znaleziono okno o nazwie '{window_title}':")
        for i, w in enumerate(window):
            print(f"Identyfikator: {w._hWnd}, Indeks: {i}")
    else:
        print(f"Nie znaleziono okna o nazwie '{window_title}'.")

def get_active_window_title():
    window_handle = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window_handle)
    return window_title, window_handle

if __name__ == "__main__":
    window_title = "polandMT2"
    #find_window_id(window_title)
    time.sleep(3)
    title, handle = get_active_window_title()
    print("Aktualnie aktywne okno:")
    print("Tytuł:", title)
    print("ID:", handle)