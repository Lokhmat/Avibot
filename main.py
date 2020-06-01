def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()
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
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

greet_bot = BotHandler('-/-')  
greetings = ('здравствуй', 'привет', 'ку', 'здорово')  
now = datetime.datetime.now()

LINKS = [
	'https://www.avito.ru/moskva_i_mo/telefony/iphone-ASgBAgICAUSeAt4J?pmax=10000000&s=104&user=1&metro=2-3-5-7-8-10-11-12-13-14-15-17-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-40-43-44-45-46-47-48-49-50-51-52-53-55-56-58-59-61-62-63-65-66-67-68-69-70-71-73-74-75-76-77-78-80-81-82-83-84-85-86-87-88-89-91-92-93-94-95-96-97-98-100-101-102-103-105-106-107-108-110-111-112-113-115-116-119-120-121-123-124-125-126-127-128-129-130-131-132-133-135-136-138-140-141-142-143-144-145-146-147-148-149-151-152-214-215-216-217-1001-1002-1003-1004-1005-1007-1008-1009-1010-1011-1012-2001-2002-2133-2135-2136-2142-2143-2144-2145-2146-2147-2148-2149-2150-2151-2152-2154-2155-2157-2158-2159-2160-2161-2162-2163-2165-2166-2167-2168-2169-2171-2172-2173-2174-2176-2177-2179-2180-2181-2182-2183-2184-2185-2186-2187-2188-2190-2191-2193-2194-2195-2199-2200-2201-2202-2203-2204-2205-2207-2208-2209-2210-2211-2212-2213-2214-2215-2219-2220-2221-2222',
  'https://www.avito.ru/moskva_i_mo/planshety_i_elektronnye_knigi/planshety-ASgBAgICAUSYAoZO?s=104&user=1&q=ipad+pro+12%2C9',
    
]

LAST_LL = [[],[]]

USERS = ['399868860', '484510136']

FLAG = [True, True]

def main():  
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        
        
        for i in range(len(LINKS)):
            if len(LAST_LL[i])>=10000:
                LAST_LL[i]=[]
            
            if i != 1:
              k = 4
              curr = get_new_block(LINKS[i],k)
              time.sleep(20)
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
              curr = get_new_block(LINKS[i],0)
              time.sleep(20)
          
              if curr not in LAST_LL:
                  LAST_LL[i]=curr
                  for user in USERS:
                      mess = str(curr)[1:-1]
                      s = ''
                      for e in mess.split(", "):
                          s = s + str(e)[1:-1] + '\n'
                      greet_bot.send_message(user,s)
        
        

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
