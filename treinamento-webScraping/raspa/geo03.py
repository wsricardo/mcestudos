from geolocation.main import GoogleMaps

google_maps = GoogleMaps(api_key='AIzaSyBCksh0B58c_C6k_Epm2k1ZQb-YF6kA6SE')

lat = -2.500044 
lng = -44.288093

location = google_maps.search(lat=lat, lng=lng)

my_location = location.first()

if my_location.city: print(my_location.city.decode('utf-8'))
if my_location.route: print(my_location.route.decode('utf-8'))
if my_location.street_number: print(my_location.street_number)
if my_location.postal_code: print(my_location.postal_code)

print(my_location.country)
print(my_location.country_shortcut)

print(my_location.formatted_address)
