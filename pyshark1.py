import pyshark

capture = pyshark.LiveCapture(interface='eth0',bpf_filter='(arp[6:2] = 2)')
capture.sniff(timeout=10)
capture

for packet in capture.sniff_continuously(packet_count=1):
    print('Just arrived:', packet)