import requests

url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

querystring = {"latlng": "40.714224,-73.96145", "language": "en"}

headers = {
    'x-rapidapi-key': "1f06abac66msh906e363b7aba314p1b2fa1jsn7924de60ec44",
    'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
