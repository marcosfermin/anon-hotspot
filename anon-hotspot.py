#!/usr/bin/env python3
#
# anon-hotspot: On demand Debian Linux (Tor) Hotspot setup tool
#
# ToDo: create new blog post?
# Blog post: http://foolcontrol.org/?p=1853
#
# Copyleft: Adnan Hodzic <adnan@hodzic.org>
# License: GPLv3

import os
import sys
from sys import argv

sep = "-" * 15
min_sep = "-" * 3
nothing = "\nNothing here yet ¯\_(ツ)_/¯\n"

def root_check():
    if not os.geteuid() == 0:
        sys.exit(f"Must be run as root, i.e: \"sudo {script}\" to run as root.")

def tor_hotspot():
    print(nothing)
    exit(0)

def hotspot():
    print(nothing)
    exit(0)

def tor():
    print(nothing)
    exit(0)

def cred():
    print(nothing)
    exit(0)

def remove():
    print(nothing)
    exit(0)

def ops_start():
    print("\nStarting Wifi Hotspot\n")
    os.system("service hostapd start")
    os.system("service dnsmasq start")
    os.system("hostapd /etc/hostapd/hostapd.conf &")
    print("[ctrl + c] to move process to background\n")

def ops_stop():
    print("\nStopping Wifi Hotspot\n")
    os.system("service tor stop")
    os.system("service hostapd stop")
    os.system("service dnsmasq stop")
    os.system("pkill hostapd")

def ops_wrong(reason):
    print(f"\n{min_sep} Error! {min_sep}\n{reason} | Aborting ...\n")
    exit(0)

def start():
    print(sep, "anon-hotspot: Debian Linux (Tor) Hotspot " + sep)
    print("\nTool usage, i.e:")
    print("anon-hotspot tor-hotspot")
    print("\n" + min_sep + " available options " + min_sep + "\n")
    print("configuration:")
    print("- tor-hotspot (configure Tor WiFi hotspot)")
    print("- hotspot (configure WiFi hotspot)")
    print("- tor (configure Tor for existing Wifi hotspot)")
    print("- cred (change Tor/WiFi Hotspot ssid/passphrase)")
    print("- remove (remove Tor/Wifi Hotspot & revert to original settings)")

    print("\noperations:")
    print("- start (start Tor/WiFi hotspot)")
    print("- stop (stop Tor/WiFi hotspot)")
    choice = input(f"{script}: ")

    if choice == "tor-hotspot":
        tor_hotspot()
    elif choice == "hotspot":
        hotspot()
    elif choice == "tor":
        tor()
    elif choice == "cred":
        cred()
    elif choice == "remove":
        remove()
    else:
        # ToDo: return wrong value and let user try again
        ops_wrong("\n\"" + choice + "\" is an unknown option")

script = argv
root_check()
start()