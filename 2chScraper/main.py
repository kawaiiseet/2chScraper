from os import makedirs
from os.path import exists

from requests import get
from json import loads


def url_processing(url):
    delimiter = "hk"
    parts = url.split(delimiter)
    base_url = parts[0] + delimiter
    return base_url


def api_json_processing(url):
    scraper = get(url)
    result = scraper.content
    js = loads(result)
    return js


def save_pictures(base_url, js, header, folder_path):
    for post in js['threads'][0]['posts']:
        if post['files'] is not None:
            for file in post['files']:
                ref = file['path']
                full_name = file['fullname']
                if ".html" not in ref and ".mp4" not in ref:
                    img_url = base_url + ref
                    print(img_url)
                    image = get(img_url, headers=header, stream=True).content
                    with open(folder_path + full_name, 'wb') as handler:
                        handler.write(image)
    print("Success")


if __name__ == '__main__':
    def main():
        header = {"User-Agent": "Mozilla/5.0"}
        print("Enter the thread url: ")
        url = input()
        print("Enter your folder path: ")
        folder_path = input()

        if ".html" in url:
            url = url.replace(".html", ".json")
        base_url = url_processing(url)
        js = api_json_processing(url)

        if not exists(folder_path):
            makedirs(folder_path)

        save_pictures(base_url, js, header, folder_path)

main()
