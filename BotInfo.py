import time

class  BotInfo:
    def __init__(self,window_id,dst_port,space_press) -> None:
        self.window_id = window_id
        self.dst_port = dst_port
        self.space_press = space_press
        self.config = True
        self.fishing = False
        self.last_trow = time.time()
        self.last_time_fishing_end = time.time()
        self.fishing_bonus = None
