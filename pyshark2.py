import pyshark

# Enable Remote Debugging
# import ptvsd
# ptvsd.enable_attach(address=("circletribe7", 3000), redirect_output=True)
# ptvsd.wait_for_attach()

capture = pyshark.LiveCapture(interface='eth0',bpf_filter='(arp[6:2] = 2)')
#capture.sniff()
#capture

def print_callback(pkt):
    #print('Just arrived:', pkt)
    #print('Just arrived:', pkt['arp'])
    #print('Just arrived:', dir(pkt.arp))
    print('Just arrived:', pkt.arp.src_hw_mac)
    #src_hw_mac


capture.apply_on_packets(print_callback)