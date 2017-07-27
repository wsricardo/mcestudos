from twitter import *

import sys
import csv

latitude = -23.5374787	# Latitude FolhaSP
longitude = -46.6456371	# Longitude Folha SP
max_range = 1 			# raio de 1km de busca
num_results = 50		# 50 resultados no mínimo
outfile = "output.csv"

twitter = Twitter(auth = OAuth("14502701-Rv3I8pkWc5MqKSc8mgRwKTUCMjXRIZTQzoSvvJlIr",
            "aZdgnQKbsmyx8IDV7B3mkl34gckpJsL84Xy76wTgnUcyQ",
            "8SUXxeyCwWBk4US1dCDZuLgpc",
            "vmuEioQX5q1RCb40kclFqpslpLkaCaIJd2xpr6VJ14AMoivNbu"))

csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)

#cabeçalho do csv
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)

result_count = 0
last_id = None
while result_count <  num_results:
	#-----------------------------------------------------------------------
	# twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets
	#-----------------------------------------------------------------------
	query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm"
                                      % (latitude, longitude, max_range),
                                      count = 100, max_id = last_id)

	for result in query["statuses"]:
		#somente processar tweets com geolocalização
		if result["geo"]:
			user = result["user"]["screen_name"]
			text = result["text"]
			text = text.encode('ascii', 'replace')
			latitude = result["geo"]["coordinates"][0]
			longitude = result["geo"]["coordinates"][1]

			row = [ user, text, latitude, longitude ]
			csvwriter.writerow(row)
			result_count += 1
		last_id = result["id"]
	print ("got %d results" % result_count)

csvfile.close()
print ("written to %s" % outfile)
