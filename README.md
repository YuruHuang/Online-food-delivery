## Online-food-delivery

This repository contains code to collect data from UberEats, Deliveroo, and JustEat. It's written using the Python Scrapy Framework and performs the following operations:

### 1. Collect all the URLs
All the available URLs are collected from the respective platforms.
**Code Example:**
\`\`\`
scrapy crawl deliveroo_new -o yourfilename.csv
\`\`\`

### 2. Delete the duplicated URLs
This step ensures that only unique URLs are retained. Similar to the code in `Deliveroo_script.py`, delete the duplicated URLs. Please update the code with your own file path.

### 3. Collect Information
Using these URLs, the code collects information for each out-of-home food outlet, such as the outlet name and cuisine types. For JustEat, there is also a Scrapy spider for collecting menu details. Update the URL file path as needed.
**Code Example:**
\`\`\`
scrapy crawl deliveroo_details -o yourfilename2.csv
\`\`\`

## Prerequisites
- **Python**
- **Scrapy**
- **Selenium Driver:** Update the path where appropriate.
- **Postcode files:** Update the path where appropriate.



