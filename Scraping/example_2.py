import requests
from bs4 import BeautifulSoup
import csv
import random
import time

csv_doc = "adverts.csv"
host = "https://www.olx.pl/"
url = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/mazowieckie"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

def get_html(url, params=''):
    req = requests.get(url, headers=headers, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("tr", class_="wrap")
    adverts = []
    for item in items:
        adverts.append(
            {
                "title": item.find("h3", class_="lheight22 margintop5").get_text().strip(),
                "link_apartment": item.find("h3", class_="lheight22 margintop5").find("a").get("href"),
                "cost": item.find("div", class_="space inlblk rel").find("p", class_="price").get_text().strip()
            }
        )
    return adverts


def save_data(items, path):
    with open(path, "w", newline='', encoding='utf-8') as csv_file:
        write = csv.writer(csv_file, delimiter=';')
        write.writerow(["Title", "Cost", "Link"])
        for item in items:
            write.writerow([item['title'], item['cost'], item['link_apartment']])


def scraper():
    pagenation = input("Specify the number of pages for parsing: ")
    pagenation = int(pagenation.strip())
    html = get_html(url)
    if html.status_code == 200:
        adverts = []
        for page in range(1, pagenation):
            print(f"Page: #{page}")
            html = get_html(url, params={"page": page})
            adverts.extend(get_content(html.text))
            time.sleep(random.randrange(2, 4))
            save_data(adverts, csv_doc)
        print("Done!")
    else:
        print("Error")


scraper()
