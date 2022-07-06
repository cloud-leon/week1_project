import requests
import pprint
import pandas as pd

url = 
    'https://s3.amazonaws.com/data-production-walltime-info/production/dynamic'
url2 = '/walltime-info.json?'

response = requests.get(url+url2)
r = response.json()
pprint.pprint(r, width=40)

pt3 = 
    f'/{last_trades_prefix}_{source_target}_{year}_{month}_{day}_{hour}_p0.json'

# the homonymous key gotten from meta.json
last_trades_prefix = 
# a trading pair (BTC-XBT or XBT-BRL, for now) user input
source_target = 
# the year you want to retrieve user input
year =
# the month of selected year
month =
# the day of selected month
day =
# the hour of the selected day in the 24-hour format
# remember to zero-pad one digit numbers (e.g. 23, 11, 01, 05)
hour =



# printing JSON to confirm success
# print(r)
# Test user input
# Test API make sure reponse is True
# output
# while with exit code zero reprompt when done
