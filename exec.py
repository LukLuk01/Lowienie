from Fishbot import Fishbot

if __name__ == "__main__":
    interface = "Ethernet"  # Zastąp "eth0" właściwą nazwą interfejsu Ethernet
    target_hex = "042b000e000000000208280"
    bot = Fishbot(interface, target_hex)
    bot.start_sniffing()
    print("other code")

