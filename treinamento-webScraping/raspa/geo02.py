from geolocation.main import GoogleMaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

origins = ['São Luis Maranhão',
           'Porto Alegre Rio Grande do Sul',
           'Belo Horizonte Minas Gerais']
destinations = ['São Paulo']

google_maps = GoogleMaps(api_key='AIzaSyBCksh0B58c_C6k_Epm2k1ZQb-YF6kA6SE')

items = google_maps.distance(origins, destinations).all()  # default mode parameter is const.MODE_DRIVING

for item in items:
    print('Origin: %s' % item.origin)
    print('Destination: %s' % item.destination)
    print('Km: %s' % item.distance.kilometers)
    print('Duration: %s' % item.duration) 
 
