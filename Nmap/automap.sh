#!/bin/bash
#
# Martin Gabriel Mejia Hurtado 17/10/22
# 2086046
#
    echo "-------------------------"
    echo "  Menu Principal"
    echo "-------------------------"
    echo "1. Escaneo de red"
    echo "2. Escaneo individual"
    echo "3. Escaneo UDP"
    echo "4. Escaneo de script"
    echo ""
read -p "Opcion [ 1 - 4 ] " c
case $c in
        1) nmap -sb $1 -oN Escaneo_de_red.txt;;
        2) nmap -v -A $1 -oN Escaneo_individual.txt;;
        3) nmap -sU $1 -oN Escaneo_UDP.txt;;
        4) nmap -v -A $1 -oN $2;;
        5) echo "Hasta luego!"; exit 0;;
esac
