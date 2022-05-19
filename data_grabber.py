import requests
import json

class noaa_explore:

    def get_NOAA_API_data(url, token):
        head = {'token':token}
        resp = requests.get(url, headers=head)
        resp_json = json.loads(resp.text)
        resp_json_results = resp_json['results']
        print(r"'response json w/ metadata' and 'results list' available as var 'json_dict' and var 'results', respectively")
        return resp_json, resp_json_results
        
    def pull_datasets():
        #get NOAA API datasets
        return noaa_explore.get_NOAA_API_data('https://www.ncei.noaa.gov/cdo-web/api/v2/datasets', 'eZzNWfQiHALrbtEHTjtzEwpGeZXPDYhV')

    def pull_stations():       
        #get NOAA API stations
        return noaa_explore.get_NOAA_API_data('https://www.ncei.noaa.gov/cdo-web/api/v2/stations','eZzNWfQiHALrbtEHTjtzEwpGeZXPDYhV')
        
    def pull_data_categories():    
        #get NOAA API data categories
        return noaa_explore.get_NOAA_API_data('https://www.ncei.noaa.gov/cdo-web/api/v2/datacategories','eZzNWfQiHALrbtEHTjtzEwpGeZXPDYhV')

class alt_pulls: 
    def pull_state_water_consump():

    def pull_sustainable_levels():

class noaa_pull:
    def pull_raindata():

    def pull_snowmelt():

    