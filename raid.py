import discord
import discord_webhook
from discord_webhook import *
import requests
import json

def mainpog():
    webhook = input("Enter  webhook url: " )
    message = input("Enter what you want to spam: ")
    delay = float(input("Enter the delay: "))
    
    while True:  
        try:
            _data = requests.post(webhook, json = {'content': message})
            if adata.status_code == 204:
                print("Sent!")
            else:
                print("Check connection")
        except:
            print("Wrong webhook")

mainpog()