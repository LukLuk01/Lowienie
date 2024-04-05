from scapy.all import *

class PacketSniffer:
    def __init__(self, interface, target_hex):
        self.interface = interface
        self.target_hex = target_hex

    def packet_callback(self, packet):
        dst_port = None
        number = None
        if IP in packet and TCP in packet:
            raw_data = bytes(packet[TCP].payload)
            if self.target_hex in raw_data.hex():
                start_index = raw_data.find(b"jeszcze")+len(b"jeszcze ")
                number_bytes = raw_data[start_index:start_index + 1]
                dst_port = packet[TCP].dport
                number = int(number_bytes.decode('utf-8'))
                return dst_port, number
    
    def start_sniffing(self):
        sniff(iface=self.interface, prn=self.packet_callback, filter="tcp and (dst port 55694 or dst port 55624) and src host 146.59.108.118")