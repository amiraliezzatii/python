import requests 
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(response.json()['data']['amount'])
print('at this time momment , bitcoin is %f dollors' % price ) 
