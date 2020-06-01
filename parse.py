import requests
from bs4 import BeautifulSoup

def get_new_block(url,k):
    site = requests.get(url)
    bs = BeautifulSoup(site.text,"html.parser")
    needed = bs.findAll("div",class_="description item_table-description")
    
    Useful = [needed[k],needed[k+1],needed[k+2]]
    Ans = []
    for useful in Useful:
        bs1 = BeautifulSoup(str(useful),"html.parser")
        name = bs1.findAll("a",class_="snippet-link")
        temp = name
        name = str(str(name).split('>')[1])[:-3]
        bs2 = BeautifulSoup(str(useful), "html.parser")
        price = bs2.findAll("span",class_="snippet-price")
        price = str(str(price).split('>')[1])[2:-9]
        link ='https://www.avito.ru' + str(str(temp).split('"')[3])
        ans = [name,price,link]
        Ans.append(ans)
    return Ans
