import requests
import json
countries_endpoint = "https://api.worldbank.org/v2/country/?format=json"
# ADD A DATE ARGUMENT TO GET A RANGE OF VALUES
gdp_endpoint = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?date=1990:2024&format=json"

base_api = "https://search.worldbank.org/api/v3/wds?format=json/country"

worldbank_indicators = [

]

# world bank countries list
def list_countries():
    countries_response = requests.get(countries_endpoint)
    json_response = json.loads(countries_response.text)
    return json_response[1]


# world bank gdp figures 1990 - 2024
def get_gdp_figures():
    gdp_response = requests.get(gdp_endpoint)
    json_response = json.loads(gdp_response.text)
    return json_response[1]


print(get_gdp_figures()) 