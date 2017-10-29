from uber_rides.session import Session
from pprint import pprint
session = Session(server_token='qZLzWGMbxgTW4uZIlE0zZ7OA2oQRwV88qyVIyi3a')

from uber_rides.client import UberRidesClient
client = UberRidesClient(session)

response = client.get_price_estimates(
    start_latitude=-23.197338,
    start_longitude=-45.892197,
    end_latitude=-23.161794,
    end_longitude=-45.795280,
    seat_count=2
)
estimate = response.json.get('prices')
print (estimate[0]['display_name'], estimate[0]['estimate'])
