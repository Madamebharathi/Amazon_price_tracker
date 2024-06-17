import requests as r
import lxml
import bs4  #library used for web scraping
from datetime import datetime
import time
import schedule

product_list=['B0CZ8SRH4Z','B0BJMGXLYZ','B07Q6153FQ']
base_url="https://www.amazon.in"
url = "https://www.amazon.in/dp/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
#A request is made to the base URL to get initial cookies
base_response=r.get(base_url,headers=headers)
cookies=base_response.cookies
#function to track prices
def track_prices():
    print(datetime.now())
    for prod in product_list:

        product_response=r.get(url+prod,headers=headers,cookies=cookies)
        soup=bs4.BeautifulSoup(product_response.text,features='lxml')
        price_lines=soup.findAll(class_="a-price-whole")
        final_price=str(price_lines[0])
        final_price=final_price.replace('<span class="a-price-whole">', '')
        final_price=final_price.replace('<span class="a-price-decimal">.</span></span>', '')
        print(url+prod,final_price)
schedule.every(5).seconds.do(track_prices)
while True:
    schedule.run_pending()
    time.sleep(1)
