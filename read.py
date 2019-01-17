import requests
from bs4 import BeautifulSoup

#Site tarafından bloklanmamak için gönderdiğimiz tarayıcı bilgileri
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


print("Lütfen bekleyin... Haberler çekiliyor...\n")

#isteğin yapılacağı adres
url= "https://www.netgazete.com/ekonomi"
istek=requests.get(url,headers)

icerik=istek.content
soup = BeautifulSoup(icerik, "lxml")

print(" LİNKlER VE  HABERLER ŞU ŞEKİLDE:\n ------------------------------")


haberler = soup.find_all("div",{"class": "altkategori-liste-haber-text"})

sayi = 1
say = 1
for i in haberler:

    print(sayi, "-)", i.text)
    sayi+=1
    #çekilen linkleri ekrana yazar
    print(i.a.get("href"))

    istek2 = requests.get(i.a.get("href"), headers)
    istek_soup = BeautifulSoup(istek2.content, "lxml")
    print(istek2.status_code,"İstek durumu")
    metin = istek_soup.find_all("div", {"id": "detail-body"})

    for j in metin:
        print(say, ".haber ---->  ", j.text)
        say += 1

    print("*"*65,"\n \n")

