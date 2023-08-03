## Online-food-delivery

<img src="https://images.unsplash.com/photo-1623123095585-bfa830e3f8a2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" width="50%">


This repository contains code to collect data from UberEats, Deliveroo, and JustEat. It's written using the Python Scrapy Framework and performs the following operations:

### 1. Collect all the URLs
All the available URLs are collected from the respective platforms.
**Code Example:**
```
scrapy crawl deliveroo_new -o yourfilename.csv
```

### 2. Delete the duplicated URLs
This step ensures that only unique URLs are retained. Similar to the code in `Deliveroo_script.py`, delete the duplicated URLs. Please update the code with your own file path.

### 3. Collect Information
Using these URLs, the code collects information for each out-of-home food outlet, such as the outlet name and cuisine types. For JustEat, there is also a Scrapy spider for collecting menu details. Update the URL file path as needed.
**Code Example:**
```
scrapy crawl deliveroo_details -o yourfilename2.csv
```

## Prerequisites
- **Python**
- **Scrapy**
- **Selenium Driver:** Update the path where appropriate.
- **Postcode files:** Update the path where appropriate.



