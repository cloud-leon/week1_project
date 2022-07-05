import requests
import pprint

# Test API by sending a Get requests
url = 'https://s3.amazonaws.com/data-production-walltime-info/production/dynamic/walltime-info.json?now=1528962473468.
679.0000000000873'
response = requests.get(url)
r = response.json()

#printing JSON to confirm success
# print(r)

#
pprint.pprint(r, width=40)


#Test user input
# Test API make sure reponse is True
#output
#while with exit code zero reprompt when done
