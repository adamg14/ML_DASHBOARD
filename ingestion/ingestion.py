import requests
import json
countries_endpoint = "https://api.worldbank.org/v2/country/?format=json"
# ADD A DATE ARGUMENT TO GET A RANGE OF VALUES
gdp_endpoint = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json"

base_api = "https://search.worldbank.org/api/v3/wds?format=json/country"

worldbank_indicators = [

]
# world bank countries list
def list_countries():
    countries_response = requests.get(countries_endpoint)
    json_response = json.loads(countries_response.text)
    return json_response[1]

def gdp():

    pass


print(list_countries()) 