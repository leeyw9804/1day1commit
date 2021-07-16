import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)

soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("div", attrs={"class":"rating_type"})

# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title, link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a["href"]
#     print(title, link)

# for cartoon in cartoons:
#     print(cartoon.get_text())
total = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    total += float(rate)
    total_rate = total/ len(cartoons)
print(total_rate)