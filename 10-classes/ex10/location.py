import requests
import json

API_KEY = "yhvQAeWy9SO0fNesp7oA63AyAEGCfRSM"
URL = "http://open.mapquestapi.com/geocoding/v1/address"

class Location:

    def __init__(self, addr):

        request_url = "{}/?key={}&location={}&maxResults=1".format(URL, API_KEY, addr)

        result = requests.get(request_url)

        if result.status_code != 200:
            raise Exception("Address not found")

        content = result.content
        content_dict = json.loads(content)

        results = content_dict["results"][0]

        location = results["locations"][0]
        
        self.userAddr = addr
        self.country = location["adminArea1"]
        self.state = location["adminArea3"]
        self.city = location["adminArea5"]
        self.postalCode = location["postalCode"]

    # Add a method to tell the user info about the location
    # Add a method to tell the user about the postalCode