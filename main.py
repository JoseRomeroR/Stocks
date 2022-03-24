import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def telegram_bot_sendtext(bot_message):
    bot_token = '000000000000000000000000000' # BOT ID
    bot_chatID = '-00000000' #destino mensaje
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


while True:
    #t0 = datetime.now().second
    #if t0%5==0:
    datetime.now()
    page = requests.get("https://www.marketwatch.com/investing/stock/dwac")
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find("h2", {"class": "intraday__price"})  #buscar valor
    resultName=soup.find("span",{"class":"company__ticker"}) #buscar nombre stock
    precioActualTexto = result.text.replace('$', '') #precio actual en texto y replace el dolar por espacio
    precioActual = float(precioActualTexto) # precio actual a float
    nombreStock=resultName.text #nombre stock
    texto=nombreStock +": "+ str((precioActual))+" $"
    test=telegram_bot_sendtext(texto)
    time.sleep(5)








