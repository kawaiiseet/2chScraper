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
        folder_path = "C:\\Users\\Свят\\Desktop\\pics"

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

        for _ in js['threads'][0]['posts']:
            i += 1
            for _ in js['threads'][0]['posts'][i]['files']:
                j += 1
                ref = js['threads'][0]['posts'][i]['files'][j]['path']
                if ".html" not in ref and ".mp4" not in ref:
                    img_url = base_url + ref
                    print(img_url)
                    download(img_url, folder_path)
            j = -1
        print("Success")
main()
