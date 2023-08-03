##################################
# delete duplicates for ubereats #
##################################

import pandas as pd 

ifps_ubereats_url = pd.read_csv('UberEats_IFPS_URLS.csv')

# Select the 'restaurant name' and 'restaurant url' columns
selected_columns = ['restaurant name', 'restaurant url']
restaurant_data = ifps_ubereats_url[selected_columns]

# Drop duplicates based on 'restaurant name' and 'restaurant url' columns
unique_restaurant_data = restaurant_data.drop_duplicates()

# 2308 records with the same restaurant url, but different restaurant names 

# Group the data by 'restaurant url' and filter groups with more than one unique 'restaurant name'
duplicate_urls = ifps_ubereats_url.groupby('restaurant url').filter(lambda x: x['restaurant name'].nunique() > 1)

# Sort the data by 'restaurant url' column
duplicate_urls = duplicate_urls.sort_values(by=['restaurant url'])

# Print the data with the same restaurant URL but different restaurant names
print(duplicate_urls)

# it looks like the names are the same for the same URL 
ifps_ubereats_url = ifps_ubereats_url.dropna(subset=['restaurant name'])

# delete the urls without outlet names 
unique_ifps_ubereats_urls = ifps_ubereats_url['restaurant url'].drop_duplicates()
unique_ifps_ubereats_urls.to_csv('UberEats_IFPS_URLS_unique.csv')