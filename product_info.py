import json
import re
from bs4 import BeautifulSoup
from typing import Dict

# Votre fonction extract_tcdata déjà corrigée
def extract_tcdata(script_content: str) -> dict:
    try:
        # Add debug print to see if we're finding tcData
        print("Searching for tcData in script content...")
        
        start_marker = "tcData  = {" if "tcData  = {" in script_content else "tcData = {"
        end_marker = "};"
        
        start_idx = script_content.find(start_marker)
        if start_idx == -1:
            print("Could not find start of tcData")
            return {}

        end_idx = script_content.find(end_marker, start_idx)
        if end_idx == -1:
            print("Could not find end of tcData")
            return {}

        json_str = script_content[start_idx + len(start_marker) - 1:end_idx + 1]
        print("Found tcData JSON:", json_str[:100] + "...") # Print first 100 chars
        
        tcdata = json.loads(json_str)
        print("Successfully parsed tcData with keys:", list(tcdata.keys()))

        key_mapping = {
            "product_price_tf": "Price_Without_Tax",
            "product_discount_ati": "Discount_Amount",
            "product_range": "Product_Range",
            "product_nature": "Product_Type",
            "product_market": "Market_Type",
            "product_target": "Target_Gender",
            "product_sku_name": "Product_Size",
            "product_rating": "Average_Rating",
            "product_promotion": "Promotion_Type",
            "product_pid_name": "Full_Product_Name"
        }

        exclude_fields = {
            'product_currency', 'product_cop', 'product_default_sku', 
            'product_axis', 'product_section', 'Currency', 
            'Product_Category', 'Section', 'product_pid', 
            'product_trademark', 
            'product_breadcrumb_label', 'product_price_ati',
            'product_subbrand', 'page_trademark', 'product_instock',
            'product_qa', 'Product_ID',
            'Brand', 'Category_Path', 'Price_With_Tax',
            'Sub_Brand', 'In_Stock', 'product_breadcrumb_id',
            'env_template', 'product_question', 'page_name',
            'page_top_cat', 'page_cat', 'page_sub_cat',
            'product_sku', 'product_sku_coverage', 'Category',
            'SubCategory', 'Product_SubCategory', 'SKU_Code',
            'Coverage_Level', 'product_video', 'product_display_type',
            'product_customizable', 'product_customized',
            'product_travel_size_availability', 'product_fidelity_points',
            'product_url_picture', 'product_num_rating', 'product_old_price_tf'
        }

        renamed_data = {}
        for old_key, value in tcdata.items():
            if old_key not in exclude_fields:
                new_key = key_mapping.get(old_key, old_key)
                if new_key not in exclude_fields:
                    renamed_data[new_key] = value
        
        print("Extracted and renamed data:", renamed_data)
        return renamed_data
    except Exception as e:
        print(f"Error extracting tcData: {str(e)}")
        return {}

# Fonction pour extraire et afficher les informations sur le parfum
def get_perfume_info(html_content: str, product_url: str = None) -> Dict[str, str]:
    perfume_info = {
        "Product_Name": None,
        "Brand": None,
        "Price": None,
        "Olfactive_Family": None,
        "Rating": None,
        "Review_Count": None,
        "Product_Label": None,
        "Product_URL": product_url
    }

    soup = BeautifulSoup(html_content, "html.parser")

    brand_element = soup.find("span", class_="brand-name", attrs={"itemprop": "name"})
    perfume_info["Brand"] = brand_element.get_text(strip=True) if brand_element else None

    name_element = soup.find("span", attrs={"itemprop": "name"}, class_=None)
    if name_element:
        full_name = name_element.get_text(strip=True)
        perfume_name = full_name.split('-')[0].strip()
        perfume_info["Product_Name"] = perfume_name

    price_element = soup.find("span", class_="price-sales-standard")
    if price_element:
        price_text = price_element.get_text(strip=True)
        price = re.sub(r'\([^)]*\)', '', price_text)
        price = price.replace('€', '').replace(',', '.').strip()
        perfume_info["Price"] = float(price)

    review_score_element = soup.find("div", class_="bv-overall-score")
    if review_score_element:
        score_text = review_score_element.get_text(strip=True)
        score = score_text.split('/')[0].strip()
        perfume_info["Rating"] = float(score)

    reviews_count_element = soup.find("span", class_="bv-number-review")
    if reviews_count_element:
        reviews_text = reviews_count_element.get_text(strip=True)
        reviews_count = reviews_text.split()[0]
        perfume_info["Review_Count"] = int(reviews_count)

    label_element = soup.find("span", class_="text-flag-label")
    perfume_info["Product_Label"] = label_element.get_text(strip=True) if label_element else None

    # Extraire et fusionner tcData
    script_elements = soup.find_all("script")
    tcdata_found = False
    print(f"Found {len(script_elements)} script tags")
    
    for i, script in enumerate(script_elements):
        if script.string:
            print(f"\nChecking script {i}:")
            if "tcData = {" in script.string or "tcData  = {" in script.string:
                print(f"Found tcData declaration in script {i}")
                tcdata = extract_tcdata(script.string)
                if tcdata:
                    tcdata_found = True
                    perfume_info.update(tcdata)
                    print("Updated perfume_info with tcData")
                break
            elif "tcData" in script.string:
                print(f"Found 'tcData' (but not declaration) in script {i}")
                print("Script content preview:", script.string[:200])
    
    if not tcdata_found:
        print("\nNo tcData declaration was found in any script tags")

    # Afficher les résultats à la fin
    print("Extracted Perfume Information:")
    print(json.dumps(perfume_info, indent=2, ensure_ascii=False))
    
    return perfume_info

# if __name__ == "__main__":
#     # Define a sample product URL for testing
#     test_product_url = "https://www.sephora.fr/p/j-adore---eau-de-parfum-P3087.html"
    
#     with open("product_page.html", "r") as file:
#         html_content = file.read()
#     get_perfume_info(html_content, test_product_url)