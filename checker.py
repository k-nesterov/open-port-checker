#!/bin/python3
import socket
import requests


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(5) # wait for N sec

   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False


def telegram_bot_sendtext(bot_message):
    # put telegram bot account token and chat id, for example
    bot_token = '1230560608:AAHxzMQcNEQQmdVx9fx5'
    bot_chatID = '@FENjkfn44uifn'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


filepath = "/app/ip_list.txt"
unreach_list = []


# check ip addresses
with open(filepath) as fp:
  for ip in fp:
    ip = ip.strip()
    status = isOpen(ip, 3389)

    if status == False:
      unreach_list.append(ip)


if len(unreach_list)>0:
  test = telegram_bot_sendtext("error server(s) unreachable " + ','.join(unreach_list))
