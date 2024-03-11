#!/bin/bash

# Define color codes
BLUE='\033[0;94m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# ASCII divider
DIVIDER="\n========================================\n"

echo -e "${GREEN}Checking service status...${NC}"
echo -e "${DIVIDER}"

echo -e "${BLUE}Nginx:${NC}"
systemctl status nginx | grep "Active"
echo -e "${DIVIDER}"

echo -e "${BLUE}WiFi:${NC}"
iwconfig wlan0 | grep ESSID
echo -e "${DIVIDER}"

echo -e "${BLUE}GSM Status:${NC}"
/home/punker/var/server/myenv/bin/python3 /home/punker/var/server/gsm.py

echo -e "${DIVIDER}"

_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "${BLUE}IP's:${NC} %s\n" "$_IP"
fi
echo -e "${DIVIDER}"

echo -e "${BLUE}Tinc:${NC}"
systemctl status tinc@tinklink | grep "Active"
echo -e "${DIVIDER}"

echo -e "${BLUE}Battery:${NC}"
/usr/bin/python3 /home/punker/var/battery.py
echo -e "${DIVIDER}"
