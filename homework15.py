import re
from unittest import result
import requests
from bs4 import BeautifulSoup

link = requests.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
soup = BeautifulSoup(link.text, "lxml")

result = soup.find_all("p")[3].text

regex = re.findall("\w+",result)

print(regex)