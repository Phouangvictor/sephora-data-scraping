import json
from bs4 import BeautifulSoup
from product_info import get_perfume_info
from product_links import get_perfume_links_from
from get_product_html import get_product_html
from get_overall_html import get_overall_html

def main():
    # List to store all perfume information
    all_perfumes_data = []
    
    try:
        # Get the overall page HTML
        print("Getting overall page HTML...")
        overall_html = get_overall_html()
        
        # Get all product links from the overall page
        print("Extracting product links...")
        product_links = get_perfume_links_from(overall_html)
        print(f"Found {len(product_links)} product links")
        
        # Process each product link
        for i, product_link in enumerate(product_links, 1):
            print(f"\nProcessing product {i}/{len(product_links)}")
            print(f"URL: {product_link}")
            
            try:
                # Get HTML content for each product
                product_html = get_product_html(product_link)
                
                # Get product information
                perfume_info = get_perfume_info(product_html, product_link)
                
                # Add to our collection
                all_perfumes_data.append(perfume_info)
                print(f"Successfully processed product {i}")
                
            except Exception as e:
                print(f"Error processing product {i}: {str(e)}")
                continue
    
        # Save all data to JSON file
        print(f"\nSaving {len(all_perfumes_data)} products to JSON...")
        with open('perfumes_data.json', 'w', encoding='utf-8') as file:
            json.dump(all_perfumes_data, file, indent=2, ensure_ascii=False)
        
        print("Data successfully saved to perfumes_data.json")

    except Exception as e:
        print(f"An error occurred in main: {str(e)}")

if __name__ == "__main__":
    main()