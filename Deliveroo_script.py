###################################
# delete duplicates for Deliveroo #
###################################

import pandas as pd 

ifps_deliveroo_url = pd.read_csv('./ubereats/Deliveroo_IFPS_2May23.csv')
ifps_deliveroo_url['rest_unique'] = ifps_deliveroo_url['restaurant url'].str.split('/').str[-1].str.split('?').str[0]

unique_ifps_deliveroo_urls = ifps_deliveroo_url.drop_duplicates(subset=['rest_unique'])
unique_ifps_deliveroo_urls.to_csv('Deliveroo_IFPS_URLS_unique.csv')