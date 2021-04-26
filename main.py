from urllib.request import Request, urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import urllib


def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) Appl    eWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=25) as f:
        data = f.read()
    return data.decode("utf-8")


def getImage(url, filename):
    image = urllib.request.urlopen(url)
    writer = image.read()
    File = open(filename + '.png', 'wb')
    File.write(writer)
    File.close

print("请输入微信公众号文章链接:")
url = input()
HtmlData = getHtml(url)
soup = BeautifulSoup(HtmlData, 'html.parser')
flag = False
metas = soup.find_all("meta")
ImageUrl = ""
ImageTitle = ""
for meta in metas:
    try:    
        pro = meta["property"]
        if pro == 'og:image':
            ImageUrl = meta['content']
        elif pro == 'og:title':
            ImageTitle = meta['content']
    except:
        continue
try:
    getImage(ImageUrl, ImageTitle)
    print("背景图获取成功,文件名为"+ImageTitle+'.png')
except:
    print("获取背景图失败QAQ")
