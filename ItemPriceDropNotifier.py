import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=sr_1_2?keywords=amd+ryzen+5+3600&qid=1578609808&sr=8-2'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}

def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    print(converted_price)
    print(title.strip())

    if(converted_price < 190):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jdotrucksyou@gmail.com', 'whcebgrypansjvhf')

    subject = 'AMD Ryzen 3600 Price has dropped!'
    body= 'Check the link! https://www.amazon.com/AMD-Ryzen-3600-12-Thread-Processor/dp/B07STGGQ18/ref=sr_1_2?keywords=amd+ryzen+5+3600&qid=1578609808&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'jdotrucksyou@gmail.com',
        'jd9redyahoo@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

check_price()

#while(True):               DELETE HASHTAGS TO DO LOOPING
#   check_price()
#   time.sleep(3)