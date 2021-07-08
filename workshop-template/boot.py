# boot.py -- run on boot-up
from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == "your_wifi_ssid":
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, "your_wifi_password"), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        print(wlan.ifconfig())
        break
