import time

from bs4 import BeautifulSoup
import requests
import json
import csv
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}


# lấy được link epi, lưu vào list rồi get link href từ các link báo đó
def get_link_articles(keywords):
    BASE_URL = 'https://baomoi.com/'
    articles_links = []

    def fetch_links(keyword):
        for i in range(1, 21):
            url = f"{BASE_URL}/{keyword}.epi"
            r = requests.get(url, headers=headers)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            a_link = soup.find_all('div', class_='bm-card-header')
            for link in a_link:
                article_link = "https://baomoi.com/" + link.a['href']
                print(article_link)
                articles_links.append(article_link)


    with ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(fetch_links, keywords)

    return articles_links

def get_json_article(articles_links):
    json_datas = []

    def fetch_html(link):
        try:
            respone = requests.get(link, headers=headers, timeout = 60)
        except requests.exceptions.Timeout:
            print("Timed out")
        html = respone.text
        json_datas.append({link: html})
        print({link: html})
        time.sleep(1.5)

    with ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(fetch_html, articles_links)

    return json_datas


def save_csv(json_datas):
    count = 0
    with open('links_html.csv', 'a', newline='', encoding='utf-8') as file:
        # Tạo một đối tượng ghi CSV
        writer = csv.writer(file)
        for data in json_datas:
            count += 1
            json_data = json.dumps(data)
            writer.writerow([json_data])
            print(count)
    print('save success')
    print(count)







