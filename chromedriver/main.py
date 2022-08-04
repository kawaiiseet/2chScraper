import cfscrape
import json
import wget
from bs4 import BeautifulSoup

print("Enter the thread url: ")
url = input()

if ".html" in url:
    url = url.replace(".html", ".json")
delimiter = "hk"
parts = url.split(delimiter)
base_url = parts[0] + delimiter

scraper = cfscrape.create_scraper()
result = scraper.get(url).content
soup = BeautifulSoup(result, 'html.parser')
js = json.loads(result)

i = -1
j = -1

for posts in js['threads'][0]['posts']:
    i += 1
    for files in js['threads'][0]['posts'][i]['files']:
        j += 1
        ref = js['threads'][0]['posts'][i]['files'][j]['path']
        if ".html" not in ref and ".mp4" not in ref:
            imgUrl = ref
            print(imgUrl)
            wget.download(base_url+imgUrl, "C:\\Users\\Свят\\Desktop\\pics")
    j = -1
i = -1
