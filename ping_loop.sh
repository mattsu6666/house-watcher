#!/bin/bash
router_address="192.168.1.1"

ping -c 10 -i 6 $router_address > /dev/null 2>&1
if [ $? -ne 0 ]; then
  python /home/pi/mail_reboot.py
  sudo reboot
fi