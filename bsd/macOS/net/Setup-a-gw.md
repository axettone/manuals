# Setup macOS as ad internet gateway

## Run on macOS as root

First enable the nat with pfctl

`echo "nat on en0 from vboxnet1:network to any -> (en0)" | pfctl -f - -e`

where `en0` is the network interface connected to the WAN and `vboxnet1` is the network device connected to the internal host.

Then enable ip forwarding

`sysctl net.inet.ip.forwarding=1`

## Run on the internal host

`route add default gw 210.100.1.2`

where `210.100.1.2` is the macOS host.


