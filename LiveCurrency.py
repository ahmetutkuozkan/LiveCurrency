import time
import requests
from bs4 import BeautifulSoup

while(True):
    #gold weight(gr) ex. first one is 10 gr second one is 20 ...
    ArrayGr = [10,20,32.5]
    #gold price(TL) ex. first one is 710 gr second one is 720 ...
    ArrayTL = [710,720,720.5]
    Result = 0
    ResultGr = 0

    #avg and sum of gold(in gr) is calculated 
    for i in range(len(ArrayGr)):
        Result += ArrayGr[i]*ArrayTL[i]
        ResultGr +=  ArrayGr[i]

    print("Avg: ",Result/ResultGr)
    print("SumGr:",ResultGr)

    #Take the gold value from website
    url="https://altin.in/fiyat/gram-altin"

    html_vaule = requests.get(url)

    All = BeautifulSoup(html_vaule.text,"html5lib")

    
    row = All.find("div",{"class":"kurlar bordernone"}).find_all("li")
    
    string_alıs = str(row[1])
    first_split = string_alıs.split(">",1)
    last_split = first_split[1].split("<",1)
    
    print("Gold price(gr/TL): ",last_split[0])
    now_TL = float(last_split[0])
    
    if((now_TL*ResultGr-Result)>0):
        print("Profit: ",(now_TL*ResultGr-Result)," TL")
    elif((now_TL*ResultGr-Result)==0):
        print("Break-even")
    else:
        print("Loss: ",(now_TL*ResultGr-Result)," TL")

    print("----------------------")

    #refresh time in sec
    time.sleep(2)
