from uber_rides.session import Session
from pprint import pprint
session = Session(server_token='qZLzWGMbxgTW4uZIlE0zZ7OA2oQRwV88qyVIyi3a')

from uber_rides.client import UberRidesClient
client = UberRidesClient(session)
response = client.get_products(-23.197338, -45.892197)
products = response.json.get('products')
for p in products:
  print ('Disponível no local:', p['display_name'])
  pprint (p['price_details'])

