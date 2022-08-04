from requests import get
from json import loads
from wget import download

print("Enter the thread url: ")
url = input()

i = -1
j = -1
folderPath = "C:\\Users\\Свят\\Desktop\\pics"

if ".html" in url:
    url = url.replace(".html", ".json")
delimiter = "hk"
parts = url.split(delimiter)
base_url = parts[0] + delimiter

scraper = get(url)
result = scraper.content
js = loads(result)

for posts in js['threads'][0]['posts']:
    i += 1
    for files in js['threads'][0]['posts'][i]['files']:
        j += 1
        ref = js['threads'][0]['posts'][i]['files'][j]['path']
        if ".html" not in ref and ".mp4" not in ref:
            imgUrl = ref
            print(imgUrl)
            download(base_url+imgUrl, folderPath)
    j = -1
i = -1
print("Success")