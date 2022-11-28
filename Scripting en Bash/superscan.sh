#!/bin/bash
# Script superscan.sh
# 24/09/22 - Martin Gabriel Mejia Hurtado
#
date
    echo "---------------------------"
    echo "   Menu Principal"
    echo "---------------------------"
    echo "1. Netdiscover"
    echo "2. PortScanv1"
    echo "3. Welcome"
    echo "4. Exit"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $HOME/netdiscover.sh;;
        2) $HOME/portscanv1.sh 192.168.121;;
        3) $HOME/welcome.sh;;
        4) echo "Bye!"; exit 0;;
