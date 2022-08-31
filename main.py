from colorama import init
init()
import time
import os
from sys import *
import requests
from multiprocessing import Process, Pool
import random
import re
import atexit
import json
import base64
try:
 from inputimeout import inputimeout,TimeoutOccurred
except:
 from setup import install
 install()
 from inputimeout import inputimeout, TimeoutOccurred
import json
try:
 from discum import *
except:
 import setup
 from discum import *
try:
 from discord_webhook import DiscordWebhook
except:
 from setup import install
 install()
 from discum_webhook import DiscordWebhook
 
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░ 
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: CoinFlip**""")
time.sleep(0.5)
print("╔═════════════════════════════════════════════════════════════════════════════════╗")
print()
print(f" {color.yellow}This is the modded auto by {color.okcyan}Iris {color.yellow}({color.okcyan}ThanhThanh2k7{color.yellow}). {color.reset}")
print(f" {color.yellow}Thanks to {color.okcyan}ahihiyou20{color.yellow} for the original version{color.reset}")
print()
print("╚═════════════════════════════════════════════════════════════════════════════════╝")
time.sleep(0.5)
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
  stopped=False
  class color:
    black  = "\033[30m"
    red    = "\033[31m"
    green  = "\033[32m"
    yellow = "\033[33m"
    blue   = "\033[34m"
    magenta= "\033[35m"
    cyan   = "\033[36m"
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
        rate = int(data["rate"])
       
        #webhook = data["webhook"]
        #webhookping = data["webhookping"]
        maxbet = data["maxbet"]
        solve = data['solve']
  current_bet = bet
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   from newdata import menu
   menu()
  print('=========================')
  print(f'|    {color.yellow}     MENU          {color.reset}|')
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
      print(f'{client.color.purple} [Modder] {client.color.reset} meangirl')
      time.sleep(10)
      exit()
else:
     print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
     time.sleep(2)
     exit()
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'

bot = discum.Client(token=client.token, log=False, build_num=0, x_fingerprint="None",user_agent=[
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:
        user = bot.gateway.session.user
        client.username=user['username']
        print("Logged in as {}{}{}#{}".format(client.color.yellow,user['username'], user['discriminator'],client.color.reset))
        print('=======================================')
        print(f'|    {client.color.blue}      INFO                    {client.color.reset}')
        print(f'| * {client.color.magenta}Username: {client.color.green}{client.username} {client.color.reset}')
        print(f'| * {client.color.magenta}Channel:{client.color.green} Id {client.channel}   {client.color.reset}')
        print(f'| * {client.color.magenta}First Bet: {client.color.green}{client.bet}  {client.color.reset}')
        print(f'| * {client.color.magenta}Rate Multiple: {client.color.green}{client.rate}  {client.color.reset}')
        print(f'| * {client.color.magenta}Max Bet Method: {client.color.green}{client.maxbet}  {client.color.reset}')
        #print(f'| * {client.color.magenta}Webhook: {client.color.green}{client.webhook}  {client.color.reset}')
        #print(f'| * {client.color.magenta}Webhookping: {client.color.green}{client.webhookping}  {client.color.reset}')
        #print(f'| * {client.color.magenta}Solve: {client.color.green}{client.solve}  {client.color.reset}')
        print('=======================================')
        print('')
        
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel and client.username in m['content'] :
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
     if '(2/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
     if '(3/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
     if '(4/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
     if '(5/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
     if 'banned' in m['content']:
      print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
     if 'complete your captcha to verify that you are human!' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      client.stopped=True
      bot.switchAccount(client.token[:-4] + 'FvBw')
      time.sleep(9999999)
      
     if  client.username in m['content'] and 'you currently have' in m['content']:
      issuechecker.cash = re.findall('[0-9]+', m['content'])
      print("{}You currently have: {} Cowoncy! {}".format(client.color.warning,','.join(issuechecker.cash[1::]),client.color.reset))
      time.sleep(3)
     if client.username in m['content'] and 'You don\'t have enough cowoncy!' in m['content']:
       print("{} [ERROR] Not Enough Cowoncy To Continue! {}".format(client.color.fail,client.color.reset))
       client.stopped=True
       bot.switchAccount(client.token[:-4] + 'FvBw')
       time.sleep(9999999)
      
        

        

@bot.gateway.command
def check(resp):
  if resp.event.message_updated:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel and m['content'] !="": 
        if  m['author']['id'] == '408785106942164992':
            if client.username in m['content'] and 'and chose' in m['content']:         
             
                if    'and you won' in m['content']:
                    print("{}[INFO WIN] Won: {} Cowoncy / {}Total Won: {} Cowoncy / {}Total Lose: {} Cowoncy  / {}Last Benefit: {} Cowoncy. {} ".format(client.color.okgreen,client.current_bet,client.color.okcyan,client.totalwon+client.current_bet,client.color.pink,client.totallost,client.color.purple,client.totalwon+client.current_bet-client.totallost,client.color.reset))
                    client.totalwon += client.current_bet
                    if client.current_bet==150000:
                        bot.typingAction(str(client.channel))
                        bot.sendMessage(str(client.channel), "owo cash")
                    client.current_bet = client.bet
                    
                    
                      
                if   'and you lost it all... :c' in m['content']:
                    print("{}[INFO LOSE] Lost: {} Cowoncy / {}Total Won: {} Cowoncy / {}Total Lose: {} Cowoncy / {}Last Benefit: {} Cowoncy. {}  ".format(client.color.fail,client.current_bet,client.color.okcyan,client.totalwon,client.color.pink,client.totallost+client.current_bet,client.color.purple,client.totalwon-client.current_bet-client.totallost,client.color.reset))
                    client.totallost += client.current_bet  
                    if client.current_bet==150000:
                      
                      bot.sendMessage(str(client.channel), "Giờ ta chẳng còn chi \nMãi trắng tay mà thôi \nĐời bạc gian lắm phủ phàng\nTiền có kiếm như nước rồi cũng sẽ trôi hết\nTay không trắng tay lại vẹn không")
                   
                      
   
                      print("{} {} [SENT] Bài ca Kiếp đỏ đen. Xin đường buồn nhé {})  ".format(at(),client.color.warning,client.current_bet,client.color.reset))
                      bot.sendMessage(str(client.channel), "owo cash")
                      if client.maxbet.lower()=="allin":
                        client.current_bet = 150000
                      if client.maxbet.lower()=="reset":
                        client.current_bet=client.bet        
                    client.current_bet *= client.rate
                    if client.current_bet>=150000:
                        client.current_bet=150000
                    time.sleep(2)
 
def cf():
    if client.stopped ==True:
        bot.switchAccount(client.token[:-4] + 'FvBw')
        time.sleep(9999999)
    else:
        if client.current_bet==150000:
            bot.sendMessage(str(client.channel), "owo pray")
        time.sleep(16)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), "owo")
        time.sleep(0.5)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), "owo cf {}  ".format(client.current_bet))
        print("{} {} [SENT] owo cf {}  ".format(at(),client.color.warning,client.current_bet))
        
        client.totalcmd += 1
        time.sleep(random.randint(wbm[0], wbm[1]))

  


  
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  pray=0
  cfwait=pray
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
