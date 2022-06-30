#!/bin/ash

iptables -A OUTPUT -p tcp --tcp-flags RST RST -s $(hostname -i) -j DROP
exec "$@"

