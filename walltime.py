import requests
import pprint
url = 'https://s3.amazonaws.com/data-production-walltime-info/production/'
url2 = 'dynamic/walltime-info.json?'

response = requests.get(url+url2)
r = response.json()
pprint.pprint(r, width=40)

# printing JSON to confirm success
# print(r)
# Test user input
# Test API make sure reponse is True
# output
# while with exit code zero reprompt when done
