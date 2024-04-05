import pygetwindow as gw

def find_window_id(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        print(f"Znaleziono okno o nazwie '{window_title}':")
        for i, w in enumerate(window):
            print(f"Identyfikator: {w._hWnd}, Indeks: {i}")
    else:
        print(f"Nie znaleziono okna o nazwie '{window_title}'.")

if __name__ == "__main__":
    window_title = "polandMT2"
    find_window_id(window_title)
