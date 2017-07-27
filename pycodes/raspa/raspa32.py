import requests

params = {'firstname': 'Fernando', 'lastname': 'Masanori'}
r = requests.post("http://pythonscraping.com/files/processing.php",
                  data=params)
#inspecionando http://pythonscraping.com/pages/files/form.html
print(r.text)
