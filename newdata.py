import time
import json
import os
from sys import exit
def menu():
 import json
 file = open("settings.json", "r")
 data = json.load(file)
 file.close()
 print('================================')
 print(f'| [0] Exit And Save           |')
 print(f'| [1] Change All Settings     |')
 print(f'| [2] Change Token            |')
 print(f'| [3] Change Channel          |')
 print(f'| [4] Change Bet Amount       |')
 print(f'| [5] Solve Capcha            |')
 print(f'| [6] Change Webhook Settings |')
 print('================================')
 choice = input("Enter Your Choice: ")
 if choice == "0":
  raise SystemExit
 if choice == "1":
  t(data,"True")
  c(data,"True")
  be(data,"True")
  solve(data,"True")
  webhook(data,"True")
 if choice == "2":
  t(data,"False")
 if choice == "3":
  c(data,"False")
 if choice == "4":
  bet(data,"False")
 if choice == "5":
  bet(data,"False")
 if choice == "6":
  bet(data,"False")
def t(data,all):
 data['token'] = input("Please Enter Your Account Token: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def c(data,all):
 data['channel'] = input("Please Enter Your Channel ID: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def bet(data,all):
 data['bet'] = input("Enter Your Bet Amount (Must Be Integer): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def solve(data, all):
 data['solve'] = input("Toggle Automatically Solve Captcha With AI (YES/NO): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def webhook(data,all):
 data['webhook'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
 if data['webhook'] != "None":
  data['webhookping'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
