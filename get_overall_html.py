import requests

def get_overall_html() -> str:
    """Get HTML content from the main perfume listing page"""
    
    url = "https://www.sephora.fr/shop/parfum-c301/"
    
    params = {
        'prefn1': 'capacities',
        'prefv1': '51 - 100 ml',
        'prefn2': 'formats',
        'prefv2': 'Flacon classique',
        'srule': 'Best sellers',
        'start': '0',
        'sz': '1000',
        'format': 'page-element',
        'on': 'onclickload',
    }
    
    headers = {
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=1, i',
        'referer': 'https://www.sephora.fr/shop/parfum-c301/?prefn1=capacities&prefv1=51%20-%20100%20ml&prefn2=formats&prefv2=Flacon%20classique&srule=Best%20sellers',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error getting overall HTML: {str(e)}")
        return ""

if __name__ == "__main__":
    html = get_overall_html()
    if html:
        print("Successfully retrieved HTML")
        with open('overall_page.html', 'w', encoding='utf-8') as f:
            f.write(html)

