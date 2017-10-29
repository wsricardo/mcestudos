from geolocation.main import GoogleMaps
address = 'São Luís Maranhão'

google_maps = GoogleMaps(api_key='AIzaSyBCksh0B58c_C6k_Epm2k1ZQb-YF6kA6SE')

location = google_maps.search(location=address)

my_location = location.first()

if my_location.city:
  print(my_location.city.decode('utf-8'))
if my_location.route:
  print(my_location.route.decode('utf-8'))
if my_location.street_number:
  print(my_location.street_number)
if my_location.postal_code:
  print(my_location.postal_code)

for administrative_area in my_location.administrative_area:
    print("%s: %s" % (administrative_area.area_type,
                      administrative_area.name.decode('utf-8')))
if my_location.country:
  print(my_location.country.decode('utf-8'))
print(my_location.country_shortcut)

print(my_location.formatted_address)

print(my_location.lat)
print(my_location.lng)
