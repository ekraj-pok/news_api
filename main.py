import requests
import pandas as pd
import apikey



api_key = apikey.api_key
url = f"https://newsapi.org/v2/everything?q=Apple&from=2023-08-09&sortBy=popularity&apiKey={api_key}"

# Make Request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
print(content["articles"])



