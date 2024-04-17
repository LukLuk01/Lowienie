import sched
import time
import threading

class SchedulerManager:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.pause_event = threading.Event()

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

def print_message(message):
    print(f"Wiadomość: {message}")

def another_function():
    print("To jest inna funkcja.")

# Utwórz instancję klasy SchedulerManager
scheduler_manager = SchedulerManager()

# Dodaj zadania do cyklicznego wykonywania
scheduler_manager.add_task(2, print_message, "Hello, world!")
scheduler_manager.add_task(5, another_function)

# Uruchom harmonogram w osobnym wątku
scheduler_manager.run()

# Główna pętla programu
while True:
    scheduler_manager.wait()
    print('program')
    time.sleep(3)
