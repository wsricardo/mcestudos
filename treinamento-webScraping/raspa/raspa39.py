from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests

html = urlopen("http://www.pythonscraping.com/humans-only")
bsObj = BeautifulSoup(html, "html.parser")
#Gather prepopulated form values
imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
formBuildId = bsObj.find("input", {"name":"form_build_id"})["value"]
captchaSid = bsObj.find("input", {"name":"captcha_sid"})["value"]
captchaToken = bsObj.find("input", {"name":"captcha_token"})["value"]

captchaUrl = "http://pythonscraping.com"+imageLocation
urlretrieve(captchaUrl, "captcha.jpg")

def verf_captcha(texto_id):
    while True:
        url_zika = "http://api.dbcapi.me/api/captcha/%s" % texto_id
        get_solved = requests.get(url_zika,timeout=5)
        texto_solved = get_solved.text
        texto_solved = texto_solved.split('&')[2].split('=')[1]
        if len(texto_solved) > 0:
            return texto_solved
        else:
            pass

data = {"username":"fmasanori","password":"labjor42"}
arq = {"captchafile":open("captcha.jpg","rb")}
req_captcha = requests.post("http://api.dbcapi.me/api/captcha", files=arq, data=data,timeout=5)
texto_id = req_captcha.text
texto_id = texto_id.split('&')[1].split('=')[1]
print (texto_id)
texto_solved = verf_captcha(texto_id)
print (texto_solved)
captchaResponse = texto_solved
print("Captcha solution attempt: "+captchaResponse)
if len(captchaResponse) == 5:
    params = {"captcha_token":captchaToken, "captcha_sid":captchaSid,   
              "form_id":"comment_node_page_form", "form_build_id": formBuildId, 
                  "captcha_response":captchaResponse, "name":"Ryan Mitchell", 
                  "subject": "I come to seek the Grail", 
                  "comment_body[und][0][value]": 
                                           "...and I am definitely not a bot"}
    r = requests.post("http://www.pythonscraping.com/comment/reply/10", 
                          data=params)
    responseObj = BeautifulSoup(r.text, 'html.parser')
    if responseObj.find("div", {"class":"messages"}) is not None:
        res = responseObj.find("div", {"class":"messages"}).get_text()
        print (res)
        if 'Error' in res:
            req_err = requests.post("http://api.dbcapi.me/api/captcha/%s" %texto_id,
                                        data=data,timeout=5)
else:
    print("There was a problem reading the CAPTCHA correctly!")
