from colorama import init
init()
import time
import os
from multiprocessing import Process, Pool
import random
import re
import atexit
import json
try:
 from discum import *
except:
 import setup
 from discum import *
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: CoinFlip**""")
wbm=[14,16]
time.sleep(0.5)
class client:
  commands=[
    "t","h"
   ]
  totalcmd = 0
  totallost = 0
  totalwon = 0
  username=""
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    pink = '\033[91m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        bet = int(data["bet"])
  current_bet = bet
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   from newdata import menu
   menu()
  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Credit            {color.reset}|')
  print('=========================')
  time.sleep(1)
choice = input('Enter your choice: ')
if choice == "1":
      pass
elif choice == "2":
      from newdata import menu
      menu()
elif choice == "3":
      print(f'{client.color.okcyan} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      time.sleep(10)
      exit()
else:
     print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
     time.sleep(2)
     exit()
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        client.username=user['username']
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      bot.gateway.close()
     if '(2/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
      bot.gateway.close()
     if '(3/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
      bot.gateway.close()
     if '(4/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
      bot.gateway.close()
     if '(5/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
      bot.gateway.close()
     if 'banned' in m['content']:
      print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
      bot.gateway.close()
     if 'complete your captcha to verify that you are human!' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      bot.gateway.close()
     if  client.username in m['content'] and 'you currently have' in m['content']:
      issuechecker.cash = re.findall('[0-9]+', m['content'])
      print("{}You currently have: {} Cowoncy! {}".format(client.color.warning,','.join(issuechecker.cash[1::]),client.color.reset))
      time.sleep(3)
     if 'You don\'t have enough cowoncy!' in m['content']:
       print("{} [ERROR] Not Enough Cowoncy To Continue! {}".format(client.color.fail,client.color.reset))
       bot.gateway.close()
@bot.gateway.command
def check(resp):
  if resp.event.message_updated:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel: 
        if client.username in m['content'] and 'and chose' in m['content']:
            if  m['author']['id'] == '408785106942164992':
             
                if    'and you won' in m['content']:
                    print("{}[INFO WIN] Won: {} Cowoncy / {}Total Won: {} Cowoncy / {}Total Lose: {} Cowoncy  / {}Last Benefit: {} Cowoncy. {} ".format(client.color.okgreen,client.current_bet,client.color.okcyan,client.totalwon+client.current_bet,client.color.pink,client.totallost,client.color.purple,client.totalwon+client.current_bet-client.totallost,client.color.reset))
                    client.totalwon += client.current_bet
                    client.current_bet = client.bet
                    
                    
                      
                if   'and you lost it all... :c' in m['content']:
                    print("{}[INFO LOSE] Lost: {} Cowoncy / {}Total Won: {} Cowoncy / {}Total Lose: {} Cowoncy / {}Last Benefit: {} Cowoncy. {}  ".format(client.color.fail,client.current_bet,client.color.okcyan,client.totalwon,client.color.pink,client.totallost+client.current_bet,client.color.purple,client.totalwon-client.current_bet-client.totallost,client.color.reset))
                    client.totallost += client.current_bet
                    client.current_bet *= 4 
 
def cf():

 
  bot.sendMessage(str(client.channel), "ocf {}  ".format(client.current_bet))
  print("{} {} [SENT] owo cf {}  ".format(at(),client.color.warning,client.current_bet))

  client.totalcmd += 1
  time.sleep(random.randint(wbm[0], wbm[1]))

  time.sleep(5)
  if client.current_bet  > 150000:
    client.current_bet = 150000
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  main=time.time()
  while x:

      cf()
      if time.time() - main > random.randint(1000, 2000):
        time.sleep(random.randint(20,30))
        main=time.time()
def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2= Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol=Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)

@atexit.register
def total():
 print("==========Stat==========")
 print("{}Total Number Of Commands Executed: {}{}".format(client.color.okcyan,client.totalcmd,client.color.reset))
 print("{}Remaining Amount Of Cowoncy: {} {}".format(client.color.okcyan,','.join(issuechecker.cash[1::]),client.color.reset)) 
 print("{}Total Lost: {} {}".format(client.color.okgreen,client.totallost,client.color.reset))
 print("{}Total Won: {} {}".format(client.color.okgreen,client.totalwon,client.color.reset))
