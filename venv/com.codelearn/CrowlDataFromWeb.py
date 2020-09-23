import requests
from bs4 import BeautifulSoup
url_value = "https://tuoitre.vn/tin-moi-nhat.htm";
response = requests.get(url_value);

#using BeautifulSoup:
soup = BeautifulSoup(response.content, "html.parser");

# Using function findAll:
titles = soup.findAll('h3', class_='title-news')

# getLink cua bai viet:
# links: chua cac link bai viet
# link: la mot bien gia do -> find(): function
# title: tieu de o ben tren
# luu cac link do vao mot mang: de tien cho viec truy vet:s
#
links = [link.find('a').attrs["href"] for link in titles]
# duyet nhung link trong bai viet:
for link in links:
    news = requests.get("https://tuoitre.vn" + link)
    soup = BeautifulSoup(news.content, "html.parser")
    title = soup.find("h1", class_="article-title").text
    abstract = soup.find("h2", class_="sapo").text
    body = soup.find("div", id="main-detail-body")
    content = body.findChildren("p", recursive=False)[0].text + body.findChildren("p", recursive=False)[1].text
    image = body.find("img").attrs["src"]
    print("Tiêu đề: " + title)
    print("Mô tả: " + abstract)
    print("Nội dung: " + content)
    print("Ảnh minh họa: " + image)
    print("_________________________________________________________________________")