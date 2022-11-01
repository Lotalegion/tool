import os
import time
import sys
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup as htmlparser
import requests
import json
import webbrowser

os.system
os.system("color 1")

def ulookup():
     Base = '[+] '
     Repl = 'repl.it:  https://replit.com/@'
     About = 'About.me:  https://about.me/'
     Github = 'Github:  https://www.github.com/'
     Codecademy = 'Codecademy: https://www.codecademy.com/profiles/'
     Roblox = 'Roblox:  https://www.roblox.com/user.aspx?username='
     Slack1 = 'Slack: https://'
     Slack2 = '.slack.com'
     Spotify = 'Spotify:  https://open.spotify.com/user/'
     Scratch = 'Scratch:  https://scratch.mit.edu/users/'
     PokemonShowdown = 'Pokemon Showdown: https://pokemonshowdown.com/users/'
     Pastebin = 'Pastebin:  https://pastebin.com/u/'
     Patreon = 'Patreon: https://www.patreon.com/'
     Steam = 'Steam:  https://steamcommunity.com/id/'
     TikTok = 'TikTok: https://tiktok.com/@'
     Giphy = 'Giphy: https://giphy.com/'
     FortniteTracker = 'FortniteTracker: https://fortnitetracker.com/profile/all/'
     Facebook = 'Facebook:  https://www.facebook.com/'
     Duolingo = 'Duolingo:  https://www.duolingo.com/profile/'

     print()
     user = input("[?] Username: ")
     print()
     print(Base + 'Finding accounts for:  ' + user)
     Repl = (Base + Repl + user)
     Github = (Base + Github + user)
     About = (Base + About + user)
     Codecademy = (Base + Codecademy + user)
     Roblox = (Base + Roblox + user)
     Slack = (Base + Slack1 + user + Slack2)
     Spotify = (Base + Spotify + user)
     Scratch = (Base + Scratch + user)
     PokemonShowdown = (Base + PokemonShowdown + user)
     Pastebin = (Base + Pastebin + user)
     Patreon = (Base + Github + user)
     Steam = (Base + Steam + user)
     TikTok = (Base + TikTok + user)
     Giphy = (Base + Giphy + user)
     FortniteTracker = (Base + FortniteTracker + user)
     Facebook = (Base + Facebook + user)
     Duolingo = (Base + Duolingo + user)

     os.system("color a")
     print()
     print(Repl)
     time.sleep(2)
     print()
     print(Github)
     time.sleep(4)
     print()
     print(About)
     time.sleep(2)
     print()
     print(Codecademy)
     time.sleep(3)
     print()
     print(Roblox)
     time.sleep(1)
     print()
     print(Slack)
     time.sleep(1)
     print()
     print(Spotify)
     time.sleep(1)
     print()
     print(Scratch)
     time.sleep(2)
     print()
     print(PokemonShowdown)
     time.sleep(4)
     print()
     print(Pastebin)
     time.sleep(3)
     print()
     print(Patreon)
     time.sleep(1)
     print()
     print(Steam)
     time.sleep(4)
     print()
     print(TikTok)
     time.sleep(2)
     print()
     print(Giphy)
     time.sleep(2)
     print()
     print(FortniteTracker)
     time.sleep(1)
     print()
     print(Facebook)
     time.sleep(3)
     print()
     print(Duolingo)
     print()
     os.system("color 1")
     input("Press any key to return to the menu!")

def plookup():
     with open('config.json', 'r') as file:
          config = json.load(file)
     apikey = config["apikey"]
     print()
     phonenumber = input("[?] Phone Number (without country code): ")
     countrycode = input("[?] Country Code: ")

     r = requests.post(f'http://apilayer.net/api/validate?access_key={apikey}&number={phonenumber}&country_code={countrycode}&format=1')
     print()
     os.system("color a")
     print(r.text)
     os.system("color 1")
     print()
     input("Press any key to return to the menu!")

def gmlookup():
     webbrowser.open("https://epieos.com/")
     os.system("color a")
     print()
     print("[+] https://epieos.com/")
     print()
     os.system("color 1")
     input("Press any key to return to the menu!")

def iplookup():
     print()
     ipv4 = input("[?] IP Address: ")
     os.system("color a")
     print()
     print("[+] https://www.iptracking.com/")
     print()
     webbrowser.open("https://www.iptracking.com/?ip_address=" + ipv4)
     os.system("color 1")
     input("Press any key to return to the menu!")

def doxcreator():
     doxname = input("[?] Dox name : ")
     name = input ("[?] Name : ")
     lastname = input("[?] LastName : ")
     age = input("[?] Age : ")
     address = input("[?] Address : ")
     supp = input("[?] More infos : ")
     fichier = open(doxname + ".txt", "a")
     fichier.write("**DOX CREATED BY THE SCRIPT**")
     fichier.write("")
     fichier.write("")
     fichier.write("---------------------------------------------------")
     fichier.write("Prenom : " + name)
     fichier.write("Nom : " + lastname)
     fichier.write("Age : " + age)
     fichier.write("Addresse : " + address)
     fichier.write("---------------------------------------------------")
     fichier.write("Infos supp")
     fichier.write("---------------------------------------------------")
     fichier.write("")
     fichier.write(supp)
     fichier.close()
     plus = input("[?] Add more infos (y/n): ")
     if plus == "y":
          supp = input("[?] More infos : ")
          fichier.write(supp)
          plus = input("[?] Add more infos (y/n): ")
          if plus == "y":
               supp = input("[?] More infos : ")
               fichier.write(supp)
               plus = input("[?] Add more infos (y/n): ")
               if plus == "y":
                    supp = input("[?] More infos : ")
                    fichier.write(supp)
                    plus = input("[?] Add more infos (y/n): ")
                    if plus == "y":
                         supp = input("[?] More infos : ")
                         fichier.write(supp)
                         plus = input("[?] Add more infos (last) (y/n): ")
                    else:
                         exit()
               else:
                    exit()
          else:
               exit()
     else:
          exit()

print()
os.system
print("""
\______ \   _______  ___ ____   __| _/ |  |   ____   ____  
 |    |  \ /  _ \  \/  // __ \ / __ |  |  | _/ __ \ / ___\ 
 |    `   (  <_> >    <\  ___// /_/ |  |  |_\  ___// /_/  >
/_______  /\____/__/\_ \\___  >____ |  |____/\___  >___  / 
        \/            \/    \/     \/            \/_____/ 
                Doxed tool
                 By Legend BS
               
 legendbs.ml
 .------------------------------------------.
 | 1.Username Searcher                      |
 | 2.Phone Lookup (require api)             |
 | 3.GMail Lookup                           |
 | 4.IP Localisation                        |
 | 5.Build dox                              |
 '------------------------------------------'
                
""")
choice = input("[?] Option: ")

if choice == "1":
     ulookup()
if choice == "2":
     plookup()
if choice == "3":
     gmlookup()
if choice == "4":
     iplookup()
if choice =="5":
     doxcreator()