#!/usr/bin/env python

import subprocess
import optparse
import re


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="Enter interface to change mac address")
    parser.add_option("--m", "--mac", dest="mac_address", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for more info.")
    elif not options.mac_address:
        parser.error("[+] Please specify a new mac address, use --help for more info")
    return options


def change_mac(interface, mac_address):
    print("[+] Changing MAC address" + interface + "to" + mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[+] Could not read mac address")


options = get_argument()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.mac_address)

current_mac = get_current_mac(options.interface)
if current_mac == options.mac_address:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[+] MAC address did not get changed.")
