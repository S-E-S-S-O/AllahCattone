# Allah Cattone. - Made by Takaso and Lojacops.
import platform         # dopo mi servono
import os
import sys
import requests
import re
from colors import *
import webbrowser
import random
import threading

agents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4429.0 Safari/537.36", "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; SGPT12 Build/TID0142) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30", "Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1853 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 HeyTapBrowser/15.7.6.1", "RadioAppFree/1563 CFNetwork/1197 Darwin/20.0.0", "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36 [ip:87.19.54.93]", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2163133002823065044 t4157550440124640339"]

title = """
%s
 ______     __         __         ______     __  __    
/\  __ \   /\ \       /\ \       /\  __ \   /\ \_\ \   
\ \  __ \  \ \ \____  \ \ \____  \ \  __ \  \ \  __ \  
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/_____/   \/_/\/_/   \/_/\/_/ 
%s                                                 
%s
 ______     ______     ______   ______   ______     __   __     ______    
/\  ___\   /\  __ \   /\__  _\ /\__  _\ /\  __ \   /\ "-.\ \   /\  ___\   
\ \ \____  \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \/\ \  \ \ \-.  \  \ \  __\   
 \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_\\"\_\  \ \_____\ 
  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_/ \/_/   \/_____/                                                                        
%s

 %s[ - Made by Takaso and Lojacops - ]%s
""" % (green(), reset(), blue(), reset(), cyan(), reset())

def search(arguments = "password"):
    dorks = open("dorks.txt", "r", encoding="UTF-8")
    for d in dorks:
        if re.search(arguments, d): print(d)

def opnn(arguments = "ssh"):
    dorks = open("dorks.txt", "r", encoding="UTF-8"); op = []
    for d in dorks:
        if re.search(arguments, d): op.append(d)
    webbrowser.open("https://www.google.com/search?q="+random.choice(op))

def open_site(siteurl, dir):
    global end
    while True:
        op = requests.get(siteurl+dir, headers={"user-agent": random.choice(agents)}).status_code
        if op in [a for a in range(200, 300)]: print(f"%s{siteurl+dir}%sKukuku... directory found." % (green(), reset()))
        if end == False:
            break

def dirfuzz(siteurl):
    global end; directories = open("directories.txt", "r", encoding="UTF-8")
    for dir in directories: end = False; p = threading.Thread(target=open_site, args=(siteurl, dir,)); p.start(); end = True
        
def random_dork():
    dorks = open("dorks.txt", "r", encoding="UTF-8").read().splitlines(); webbrowser.open("https://www.google.com/search?q="+random.choice(dorks))

def main():
    print(f"""
{title}

    Commands:
    sesso_search => Searches a dork in the list.
    sesso_dork => Tries a dork.
    exit => Exits the tool.
    sessopen => Vulerability to find.
    dirsesso => Searches directories in a site.
    random_dork => Tries a random google dork.
    """)
    while True:
        prompt = input('%sAllah%s%s@%s%sCattone%s> ' % (green(), reset(), yellow(), reset(), blue(), reset()))
        if prompt.startswith("sesso_search"):
            a = prompt.replace("sesso_search", ""); b = a.replace(" ", ""); search(b)
        elif prompt == "sesso_dork":
            print("Types of dorks:")
            print("""
            1) allintext + target
            2) intext + target
            3) le prime due ma con il sito specificatohh (site: google.com)
            """) 
            dork_create_option = input('Create > '); webbrowser.open("https://www.google.com/search?q="+dork_create_option)
        elif prompt == "exit":
            sys.exit()
        elif prompt.startswith("sessopen"):
            a = prompt.replace("sessopen", ""); b = a.replace(" ", ""); opnn(b)
        elif prompt.startswith("dirsesso"):
            a = prompt.replace("dirsesso", ""); b = a.replace(" ", ""); dirfuzz(a)
        elif prompt.startswith("random_dork"):
            random_dork()
        else:
            print("sus.")

main()