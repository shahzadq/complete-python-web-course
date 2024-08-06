import requests
from bs4 import BeautifulSoup

_author_ = 'Shahzad Qureshi'

request = requests.get(
    "https://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

if price < 200:
    print('Chair in budget')
    print('The current price is {}'.format(string_price))
else:
    print('Chair not in budget')
    print('The current price is {}'.format(string_price))

# <span itemprop="price" class="now-price"> £229.00 </span>
