from crawl import get_link_articles, get_json_article, save_csv
import time
from list_xml_links import get_link_epi,get_keyword



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

# url ='https://baomoi.com/sitemaps/sitemap.xml?gidzl=xXAJ04auuXph3904IIBg7UCEdWHUT-iI_mZB3GbpwaRuNiyBNo6x4wfOcWi1TU17yLQKNpYJ6aClJplb5W'

list_link = ['https://baomoi.com/sitemaps/category.xml',
             'https://baomoi.com/sitemaps/publisher.xml',
             'https://baomoi.com/sitemaps/region.xml']


# Lấy các link chứa từ khóa 'epi'



# response = requests.get(url, headers=headers)
# xml_data = response.text
#
# # Parse XML data từ response.text
# root = ET.fromstring(xml_data)
#
# # Lọc ra các link chứa từ khóa 'article'
# article_links = [element.text for element in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc') if 'article' in element.text]

def main():
    start = time.time()
    epi_links = get_link_epi(list_link)
    keywords = get_keyword(epi_links)
    link_articles = get_link_articles(keywords)
    print("time to count down 30s:", time.sleep(30))
    articles_htmls = get_json_article(link_articles)
    save_csv(articles_htmls)
    end = time.time()
    print(f"Time: {end - start}")

if __name__ == "__main__":
    main()