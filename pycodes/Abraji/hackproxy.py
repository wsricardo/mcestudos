import urllib.request as req
proxy = req.ProxyHandler({'http': r'http://abraji:abraji2015@192.168.0.11:3128'})
auth = req.HTTPBasicAuthHandler()
opener = req.build_opener(proxy, auth, req.HTTPHandler)
req.install_opener(opener)

