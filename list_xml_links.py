
import requests
import time
import xml.etree.ElementTree as ET
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}


# lấy link epi từ các link xml

def get_link_epi(list_link):
    epi_links = []
    for link in list_link:
        response = requests.get(link, headers=headers)
        xml_data = response.text
    # Parse XML data từ response.text
        root = ET.fromstring(xml_data)
        # tìm các link có đuôi epi
        link = [element.text for element in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc') if
                         'epi' in element.text]
        epi_links.extend(link)
    return epi_links




# link có dạng này, cần phải lấy từ khóa sau baomoi.com/rồi thêm .epi để lấy link bài báo

# Pattern regex để lấy từ khóa
pattern = r"baomoi\.com/(.*?)\.epi"

# Lặp qua các đường link và lấy từ khóa

def get_keyword(links):
    keywords = []
    for link in links:
        match = re.search(pattern, link)
        if match:
            keyword = match.group(1)
            keywords.append(keyword)
    return keywords
