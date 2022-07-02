import requests

# Test API by sending a Get requests
url = 'https://s3.amazonaws.com/data-production-walltime-info/production/dynamic/walltime-info.json?now=1528962473468.679.0000000000873'
response = requests.get(url)

#printing JSON to confirm success
print(response.json)