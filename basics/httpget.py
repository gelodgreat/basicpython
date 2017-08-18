import requests
from bs4 import BeautifulSoup

myRequest = requests.get("https://tipidpc.com/viewitem.php?iid=41811610")
content = myRequest.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("h2", {"class": "itemprice"})

detectedPrice = element.text.strip()
price_without_symbol = detectedPrice[4:]
myPrice = float(price_without_symbol)

print (detectedPrice)

if (myPrice <= 1000):
    print ("Buy it")
    print ("The current price is {}".format(detectedPrice))
else:
    print ("It's expensive")
    print ("The current price is {}".format(detectedPrice))

# Getting all content
# print(request.content)
