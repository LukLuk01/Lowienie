from pywinauto import application

def activate_window_by_id(window_id):
    try:
        app = application.Application()
        app.connect(handle=window_id)
        window = app.window(handle=window_id)
        window.set_focus()
        print("Okno zostało aktywowane.")
    except Exception as e:
        print("Wystąpił błąd:", e)

if __name__ == "__main__":
    window_id = 131584  # Wprowadź identyfikator okna
    activate_window_by_id(window_id)
