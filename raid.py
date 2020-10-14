import random
import string
import discord
import discord_webhook
from discord_webhook import *
import requests
import json
import time

def mainheh():
    print("""
    fuck this server lets spam
    """)
    print(" ")
    Webhook = input("Enter the webhook url: " )
    Message = input("Enter what you want to spam: ")
    delay = float(input("Enter the delay: "))
    
    while True:
        print("Sending: " + Message)
        print("Sending to: " + Webhook)
        print("Delay: " + str(delay))
        
        try:
            _data = requests.post(Webhook, json = {'content': Message})
            if adata.status_code == 204:
                print("Sent!")
            else:
                print("Check connection")
        except:
            print("Wrong webhook")

mainheh()