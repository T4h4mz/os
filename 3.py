from scapy.all import *
import time

packets_received = 0
packets_sent = 0

def packet_function(packet):
    global packets_received
    if packet.haslayer(IP):
        packets_received = packets_received + 1


target_ip = '192.168.1.1'
ping_pkt = IP(dst=target_ip)/ICMP()
send(ping_pkt)



start_time = time.time()
while time.time() - start_time < 11:
    sniff(prn=packet_function, timeout=1)
    packets_sent += 1
    ping_pkt = IP(dst=target_ip)/ICMP()
    send(ping_pkt)


print(f"packets_received: {packets_received} - packets_sent: {packets_sent}")
