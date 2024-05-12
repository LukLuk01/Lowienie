from scapy.all import *
from queue import Queue


class PacketSniffer:
    def __init__(self, interface, target_ip, target_hex,fishing_end_info_unsucces,fising_end_info_succes):
        self.interface = interface
        self.target_hex = target_hex
        self.fishing_end_info_unsucces =fishing_end_info_unsucces
        self.fising_end_info_succes =fising_end_info_succes
        self.data_queue = Queue()
        self.fishing_info_queue = Queue()
        self.target_ip = target_ip
        self.pulling = False
        self.unique_ports = set()  # Zbiór do przechowywania unikalnych portów

    def packet_callback(self, packet):
        dst_port = None
        number = None
        state = False
        if IP in packet and TCP in packet: # type: ignore
            raw_data = bytes(packet[TCP].payload) # type: ignore
            if self.target_hex in raw_data.hex():
                print(len(raw_data.hex()))
                start_index = raw_data.find(b"jeszcze")+len(b"jeszcze ")
                number_bytes = raw_data[start_index:start_index + 1]
                dst_port = packet[TCP].dport # type: ignore
                number = int(number_bytes.decode('utf-8'))
                self.data_queue.put((dst_port, number))
                print(f"---odebrano pakiet {dst_port}----\n")
                if self.fishing_end_info_unsucces in raw_data.hex():
                    state = False
                    dst_port = packet[TCP].dport # type: ignore
                    self.fishing_info_queue.put((dst_port, state))
                if self.fising_end_info_succes in raw_data.hex():
                    state = True
                    dst_port = packet[TCP].dport # type: ignore
                    self.fishing_info_queue.put((dst_port, state))


    def start_sniffing(self):
        #sniff(iface=self.interface, prn=self.packet_callback, filter="tcp and (dst port 63168 or dst port 63756 or dst port 62821) and src host 146.59.108.118")
        sniff(iface=self.interface, prn=self.packet_callback, filter=("tcp and src host 146.59.108.118"))

    def check_tcp_ports(self):
        start_time = time.time()
    
        # Nasłuchiwanie na przychodzące pakiety TCP przez 10 sekund
        while time.time() - start_time < 7:
            try:
                packet = sniff(filter="tcp and src host " + self.target_ip, count=1, timeout=1)
                if packet:
                    source_port = packet[0][TCP].dport # type: ignore
                    self.unique_ports.add(source_port)
            except KeyboardInterrupt:
                break
        return self.unique_ports

    def update_status(self,port):
        self.pulling = False