#!/usr/bin/env python
from python_arptable import get_arp_table

# Enable Remote Debugging
#import ptvsd
#ptvsd.enable_attach(address=("circletribe7", 3000), redirect_output=True)
#ptvsd.wait_for_attach()

print(get_arp_table())