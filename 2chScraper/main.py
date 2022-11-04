import urllib.request
from os import makedirs
from os.path import exists

from requests import get
from json import loads
from wget import download

if __name__ == '__main__':
    def main():
        print("Enter the thread url: ")
        url = input()

        i = -1
        j = -1
        folder_path = "" # your folder path with '//' at the end
        header = {"User-Agent": "Mozilla/5.0"}
        if ".html" in url:
            url = url.replace(".html", ".json")
        delimiter = "hk"
        parts = url.split(delimiter)
        base_url = parts[0] + delimiter

        scraper = get(url)
        result = scraper.content
        js = loads(result)

        if not exists(folder_path):
            makedirs(folder_path)

        for post in js['threads'][0]['posts']:
            if post['files'] is not None:
                for file in post['files']:
                    ref = file['path']
                    full_name = file['fullname']
                    j += 1
                    if ".html" not in ref and ".mp4" not in ref:
                        img_url = base_url + ref
                        print(img_url)
                        image = get(img_url, headers=header, stream=True).content
                        with open(folder_path + full_name, 'wb') as handler:
                            handler.write(image)
        print("Success")

main()
