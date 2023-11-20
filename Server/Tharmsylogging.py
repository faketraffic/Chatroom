# logging API
# Author: Tharmsy
# Date: 20/11/2023
# Version: 1.0.0

import colorama # useless but whyever
from colorama import init, Fore

def initialize():
    init(convert=True)

def info(msg):
    print(Fore.LIGHTBLACK_EX + '[*] ' + Fore.RESET + str(msg))

def error(msg):
    print(Fore.LIGHTRED_EX + '[-] ' + Fore.RESET + str(msg))

def good(msg):
    print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.RESET + str(msg))