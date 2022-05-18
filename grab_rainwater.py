from matplotlib.pyplot import get
import requests
import json

def get_NOAA_API_data(url, token):
    head = {'token':token}
    resp = requests.get(url, headers=head)
    resp_json = json.loads(resp.text)
    resp_json_results = resp_json['results']
    print(r"'response json w/ metadata' and 'results list' available as var 'json_dict' and var 'results', respectively")
    return resp_json, resp_json_results
    
def pull_datasets():
    #get NOAA API datasets
    return(get_NOAA_API_data('https://www.ncei.noaa.gov/cdo-web/api/v2/datasets', 'eZzNWfQiHALrbtEHTjtzEwpGeZXPDYhV'))

def pull_stations():       
    #get NOAA API stations
    return(json_dict, results = get_NOAA_API_data('https://www.ncei.noaa.gov/cdo-web/api/v2/stations','eZzNWfQiHALrbtEHTjtzEwpGeZXPDYhV'))
    
def pull_data_categories():    
    #get NOAA API data categories
    return(get_NOAA_API_data('https://www.ncei.noaa.gov/cdo-web/api/v2/datacategories','eZzNWfQiHALrbtEHTjtzEwpGeZXPDYhV'))