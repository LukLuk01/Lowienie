import threading
import sched
import time
import pydirectinput
import random

def add_5_prc_bonus(scheduler):
    pydirectinput.typewrite('2')
    scheduler.enter(1800, 1, add_5_prc_bonus, (scheduler,))  # Zaplanuj kolejne naciśnięcie klawisza "2" za 30 minut

# Utwórz planistę zadań
scheduler = sched.scheduler(time.time, time.sleep)

# Rozpocznij wykonywanie funkcji press_key_2 co 30 minut
scheduler.enter(1800, 1, add_5_prc_bonus, (scheduler,))
key_press_thread = threading.Thread(target=scheduler.run)
key_press_thread.daemon = True  # Ustawienie wątku jako demon

# Uruchom wątek
key_press_thread.start()

# Tutaj wklej swój kod główny

if __name__ == "__main__":
    while True:
        print('mienla sekunda')
        time.sleep(1)
    
    # Tutaj wklej resztę swojego kodu
