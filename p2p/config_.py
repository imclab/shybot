#
# change this file to config.py
# you need two or more nodes for p2p sync

import landerdb
import socket
import random

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com", 80))
    local_ip = s.getsockname()[0]
    s.close()
except:
    local_ip = "127.0.0.1"

# name your node
label = "peer%d" % int(random.random()*100)
sleep_time = 5  # lower the faster syncing with peers

# master node needs to be a relay
relay = 1  # set this to zero to "not" relay to other nodes (aka leaf node).
seeds = []  # master has no seeds
version = "0.0.1"
host = local_ip
port = 6565
nodes = landerdb.Connect("nodes.db")

print "%s:%d" % (host, port)
