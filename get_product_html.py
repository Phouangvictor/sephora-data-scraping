import requests

def get_product_html(url: str) -> str:
    """Get HTML content from a product page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except Exception as e:
        print(f"Error getting product HTML: {str(e)}")
        return ""

if __name__ == "__main__":
    # Test the function
    url = "https://www.sephora.fr/p/j-adore---eau-de-parfum-71393.html"
    html = get_product_html(url)
    if html:
        print("Successfully retrieved HTML")
        with open('product_page.html', 'w', encoding='utf-8') as f:
            f.write(html)