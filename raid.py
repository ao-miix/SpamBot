import discord
import discord_webhook
from discord_webhook import *
import requests
import json

def mainheh():
    print("""

██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ░██████╗██████╗░░█████╗░███╗░░░███╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗████╗░████║
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ╚█████╗░██████╔╝███████║██╔████╔██║
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░
    -simple webhook spammer 
    - made by arav :)
    """)
    print(" ")
    Webhook = input("Enter  webhook url: " )
    Message = input("Enter what you want to spam: ")
    delay = float(input("Enter the delay: "))
    
    while True:

        
        try:
            _data = requests.post(Webhook, json = {'content': Message})
            if adata.status_code == 204:
                print("Sent!")
            else:
                print("Check connection")
        except:
            pass
mainheh()