import foursquare
client = foursquare.Foursquare(client_id='R11WEB4V5HLSLSRLF5WI3BHSRHUPLBSOISG32FOBXLFWDRVZ',
                               client_secret='IAWP4BSJ1FIZC1NDPOQACPAZVY52WTYDIWXS3QUBLWUBSA3V')
auth_uri = client.oauth.auth_url()
res = client.venues.search(params={'ll':'-2.500044, -44.288093',
                                   'query':'pizza',
                                   'radius':'2000'})
for x in res['venues']:
  print (x['name'], x['location']['formattedAddress'][0])
