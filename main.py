import requests
from tabulate import tabulate

API_KEY = 'LtPYEsjsHiSlnn2EwYTVRMOtgYKSlBJ21sQXr3HD'
url = 'https://api.watchmode.com/v1/search/'

while True:
    name=input("Enter the movie to search: ")

    params = {
        'apiKey': API_KEY,
        'search_field': 'name',
        'search_value': name
    }

    response = requests.get(url, params=params)

    search_results = response.json()
    if search_results['title_results']:
        movie_id = search_results['title_results'][0]['id']
    else:
        print("Movie not found.")

    sources_url = f'https://api.watchmode.com/v1/title/{movie_id}/sources/'
    sources_params = {
        'apiKey': API_KEY
    }

    sources_response = requests.get(sources_url, params=sources_params)

    streaming_sources = sources_response.json()
    table_data = []
    for source in streaming_sources:
        table_data.append([source['name'], source['type'], source['price']])

    # Define table headers
    headers = ["Platform", "Type", "Price"]

    # Display the table
    print(tabulate(table_data, headers, tablefmt="pretty"))