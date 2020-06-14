#!/usr/bin/env python

import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="Enter interface to change mac address")
    parser.add_option("--m", "--mac", dest="mac_address", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, mac_address):
    print("[+] Changing MAC address" + interface + "to" + mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


(options, arguments) = get_argument()

change_mac(options.interface, options.mac_address)
