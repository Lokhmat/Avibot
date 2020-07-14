
from another import get_new_block
import requests  
import datetime
import time

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        try:
           
            resp = requests.post(self.api_url + method, params)
            return resp
        except Exception:
            print('failed to connect')
            return 1

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler('-//-')  
greetings = ('здравствуй', 'привет', 'ку', 'здорово')  
now = datetime.datetime.now()

LINKS = []

LAST_LL = [[],[]]

USERS = []

FLAG = [True, True]

def main():  
    new_offset = None
    today = now.day
    hour = now.hour
    
    while True:
        
        
        for i in range(len(LINKS)):
            if len(LAST_LL[i])%100==0:
                greet_bot.send_message('',str(len(LAST_LL[i])))
            
            
            if i == 0:
              k = 4
              try:
                curr = get_new_block(LINKS[i],k)
                time.sleep(20)
              except Exception:
                print(Exception)
                greet_bot.send_message('','Ia upal')
              for j in range(len(curr)):
                if curr[j] not in LAST_LL[i]:
                    LAST_LL[i].append(curr[j])
                    for user in USERS:
                        mess = str(curr[j])[1:-1]
                        s = ''
                        for e in mess.split(", "):
                            s = s + str(e)[1:-1] + '\n'
                        greet_bot.send_message(user,s)
            else:
              k = 0
              try:
                curr = get_new_block(LINKS[i],k)
                time.sleep(20)
              except Exception:
                print(Exception)
                greet_bot.send_message('','Ia upal')
              for j in range(len(curr)):
                if curr[j] not in LAST_LL[i]:
                    LAST_LL[i].append(curr[j])
                    for user in USERS:
                        mess = str(curr[j])[1:-1]
                        s = ''
                        for e in mess.split(", "):
                            s = s + str(e)[1:-1] + '\n'
                        greet_bot.send_message(user,s)
            

                '''
              try:  
                curr = get_new_block(LINKS[i],0)
                time.sleep(20)
              except Exception:
                print(Exception)
                greet_bot.send_message('','Ia upal')
                
                
              if curr not in LAST_LL:
                  LAST_LL[i]=curr
                  for user in USERS:
                      mess = str(curr)[1:-1]
                      s = ''
                      for e in mess.split(", "):
                          s = s + str(e)[1:-1] + '\n'
                      greet_bot.send_message(user,s)
                      '''
        
        

def setup():
    for user in USERS:
            greet_bot.send_message(user,'Первичная настройка')
    for link in LINKS:
        
        curr = get_new_block(link,4)
        time.sleep(10)
        LAST_LL.append(curr)
        mess = str(curr[0])[1:-1]
        s = ''
        for e in mess.split(", "):
            s = s + str(e)[1:-1] + '\n'
        for user in USERS:
            
            greet_bot.send_message(user,s)
    for user in USERS:
            greet_bot.send_message(user,'работаю')

if __name__ == '__main__':
    
    try:
        print('Производится настройка')
        setup()
        print('Я должен жить')
        main()
    except KeyboardInterrupt:
        exit()
