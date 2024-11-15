# Sephora Perfume Scraper: Uncovering Fragrance Trends
![Symbole-Sephora](https://github.com/user-attachments/assets/c9326c9d-1b10-4805-803a-1971b3b56eae)

**Dive into the World of Fragrances with this Python-Powered Scraper**

This project was born out of a fascinating challenge in my Python programming course at  Eugenia School: **to extract and analyze data from Sephora's extensive perfume collection.** I wanted to go beyond a simple scraping exercise and uncover potential trends in the fragrance world. To make the project more manageable and insightful, I decided to focus on a specific segment of Sephora's perfume offerings:

# Criteria:

**Volume:** 50ml or 100ml (the most common sizes)
**Flacon Type:** Classic (to maintain consistency and avoid confusing variations like rollerballs or travel sprays)

**Why these criteria?**
By focusing on these specific criteria, I aimed to **create a dataset** that would allow me to compare similar products and potentially identify trends within a more uniform selection of perfumes.

<img width="1494" alt="Screenshot 2024-11-15 at 10 13 50" src="https://github.com/user-attachments/assets/a7236dab-b76e-4664-a4f9-814b560168c8">

# Data Points Extracted: #
My scraper delves deep into Sephora's product pages to extract a wealth of information, including:

**Product name:** The actual name of the fragrance.
**Brand:** The brand behind the fragrance.
**Price:** Both with and without tax.
**Discount amount:** To identify potential patterns in discounts or promotions.
**Average rating:** To gauge overall customer satisfaction.
**Number of reviews:** To assess the popularity and feedback volume of a fragrance.
**Product label:** Identifying "Bestseller" or other promotional labels.
**Full product name:** The complete product name as listed on Sephora.
**Product Type:** Whether it's an eau de parfum, eau de toilette, etc.
**Market Type:** Selective or exclusive, to understand distribution strategies.
**Target Gender:** Male, female, or mixed.

**And more!**


# A Peek Under the Hood: Files and Functionality #
**main.py:** The script that orchestrates the entire scraping process.
**product_info.py:** Contains functions to extract detailed product information from individual product pages.
**product_links.py:** Extracts all the links to individual perfume pages from the main product listing page.
**get_product_html.py:** Fetches the raw HTML content from each product page.
**get_overall_html.py:** Fetches the raw HTML content from the main perfume listing page.
**perfumes_data.json:** A sample data output file in JSON format to illustrate the structure and content of the scraped data.

# Running the Scraper: #
**Install necessary libraries:** Make sure you have requests, beautifulsoup4 and json installed. You can install them using pip: pip install requests beautifulsoup4.

**Execute the main.py script:** This will initiate the scraping process, fetching the main page HTML, extracting product links, and then scraping data from each individual product page.

**Output:** The scraped data will be saved in perfumes_data.json.

# Challenges and Triumphs: #
**Dynamic Loading:** One of the major hurdles was handling Sephora's dynamic product loading, where new products appear as you scroll down the page. To tackle this, I leveraged AI-powered code generation tools to create a solution that effectively captures all products.

# Respecting robots.txt: #
**Rate Limiting:** To ensure compliance with Sephora's robots.txt, I implemented delays between requests, preventing overload on their servers and demonstrating responsible scraping practices.

# Data Cleaning and Pagination: #

**Cleaning for Visualization:** After scraping, a dedicated function was used to clean the raw data, ensuring it seamlessly integrates with our preferred data visualization tools.

**Pagination:** To handle large product sets (over 1000), I adjusted the pagination parameters in the get_overall_html.py file, allowing the scraper to navigate through multiple pages and collect all relevant links.

# Potential Use Cases: #
**The data I've collected has exciting potential for:**

**Market Research:** Understanding current trends in perfume preferences, pricing strategies, and popular brands.

**Business Strategy:** Driving data-driven decisions related to product development, marketing campaigns, and inventory management.

**Personal Project:** Exploring personal fragrance preferences, discovering new scents, and conducting further analysis.

# Gratitude and Acknowledgements: #

I'd like to express my sincere gratitude to Eugenia School and our fantastic teacher for providing this enriching learning opportunity.

# Important Notes: #
**Ethical Scraping:** This project is designed for educational purposes and to showcase web scraping techniques. Please use it responsibly and ethically, respecting Sephora's robots.txt and terms of service.

**Data Freshness:** The perfumes_data.json file contains sample data; it's a snapshot in time and may not be up-to-date. Running the scraper will fetch the latest information from Sephora.

**Contributions and Issues:** Feel free to contribute to the project by reporting any issues you encounter or by suggesting improvements.

**Let's explore the fragrant world of perfumes together!**

**Here is the links and images of our dashboards :** 
https://public.tableau.com/shared/H9B2CB9DM?:display_count=n&:origin=viz_share_link 

<div class='tableauPlaceholder' id='viz1731661871601' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;38&#47;386HKP8WS&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;386HKP8WS' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;38&#47;386HKP8WS&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                

<div class='tableauPlaceholder' id='viz1731661921438' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4Z&#47;4ZK897MZT&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;4ZK897MZT' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;4Z&#47;4ZK897MZT&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                

<div class='tableauPlaceholder' id='viz1731661478665' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;J9&#47;J9R7HJXM9&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;J9R7HJXM9' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;J9&#47;J9R7HJXM9&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                
