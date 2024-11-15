from bs4 import BeautifulSoup
from typing import List

def get_perfume_links_from(html_content: str) -> List[str]:
    links = []

    soup = BeautifulSoup(html_content, "html.parser")
    product_info_divs = soup.find_all("div", class_="product-info")

    for product_div in product_info_divs:
        product_link = product_div.find("a", class_="product-tile-link")
        if product_link and product_link.get("href"):
            url = product_link.get("href")
            links.append(url)

    return links

if __name__ == "__main__":
    with open("overall_page.html", "r") as file:
        html_content = file.read()

    product_links = get_perfume_links_from(html_content)
#     # for url in product_links:
#     #     print(url)
    
    print(f"\nTotal links scraped: {len(product_links)}")