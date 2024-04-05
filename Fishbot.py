from PacketSniffer import PacketSniffer

class Fishbot:
    def __init__(self, interface, target_hex):
        self.interface = interface
        self.target_hex = target_hex
        self.sniffer = PacketSniffer(interface, target_hex)

    def bot_exec(self, dst_port, number):
        print("Metoda bot_exec() została wywołana z dst_port:", dst_port, "i number:", number)

    def start_sniffing(self):
        self.sniffer.start_sniffing()