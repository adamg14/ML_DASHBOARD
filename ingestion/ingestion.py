import requests
import json

# ENDPOINTS
countries_endpoint = "https://api.worldbank.org/v2/country/?format=json"
gdp_endpoint = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?date=1990:2024&format=json"
population_endpoint = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=1990:2024&format=json"
base_api = "https://search.worldbank.org/api/v3/wds?format=json/country"

worldbank_indicators = [

]

# world bank countries list
def get_countries_list():
    countries_response = requests.get(countries_endpoint)
    json_response = json.loads(countries_response.text)
    return json_response[1]


# world bank gdp figures 1990 - 2024
def get_gdp_figures():
    gdp_response = requests.get(gdp_endpoint)
    json_response = json.loads(gdp_response.text)
    return json_response[1]


def get_population_figures():
    pop_response = requests.get(population_endpoint)
    json_response = json.loads(pop_response.text)
    return json_response[1]


print(get_population_figures()) 