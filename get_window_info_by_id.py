import pygetwindow as gw

def get_window_info_by_id(window_id):
    try:
        window = gw.win32wrapper.GetWindow(window_id)
        if window:
            window_info = {
                "Title": window.title,
                "ID": window_id,
                "Position": (window.left, window.top),
                "Size": (window.width, window.height)
            }
            return window_info
        else:
            return None
    except Exception as e:
        print("Wystąpił błąd:", e)

if __name__ == "__main__":
    window_id = 525240  # Wprowadź identyfikator okna
    window_info = get_window_info_by_id(window_id)
    if window_info:
        print("Informacje o oknie:")
        print(window_info)
    else:
        print("Nie znaleziono okna o podanym ID.")
