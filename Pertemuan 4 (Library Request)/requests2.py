import requests

req = requests.get("https://stikombanyuwangi.ac.id/")
req.encoding
req.status_code
req.elapsed
req.url
req.headers
req.history
print(req.history)