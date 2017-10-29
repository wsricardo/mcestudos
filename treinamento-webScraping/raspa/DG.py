from uber_rides.session import Session
session = Session(server_token='qZLzWGMbxgTW4uZIlE0zZ7OA2oQRwV88qyVIyi3a')
from uber_rides.client import UberRidesClient
client = UberRidesClient(session)

response = client.get_price_estimates(
    start_latitude=-19.634129, 
    start_longitude=-43.965375,
    end_latitude=-19.919194, 
    end_longitude=-43.936129,
    seat_count=2
)
estimate = response.json.get('prices')
print (estimate)
print (estimate[0]['display_name'], estimate[0]['estimate'])
