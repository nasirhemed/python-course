from urllib import request, parse
import json

API_KEY = "yhvQAeWy9SO0fNesp7oA63AyAEGCfRSM"
URL = "http://open.mapquestapi.com/geocoding/v1/address/"

class Location:

    def __init__(self, addr):
        
        request_params = {
            "key" : API_KEY,
            "location": addr,
            "maxResults": 1
        }

        encoded_url = URL + "?" + parse.urlencode(request_params)

        result = request.urlopen(encoded_url)

        if result.getcode() != 200:
            raise Exception("Address not found")

        content = result.read()
        content_dict = json.loads(content)

        results = content_dict["results"][0]

        location = results["locations"][0]
        
        self.userAddr = addr
        self.country = location["adminArea1"]
        self.state = location["adminArea3"]
        self.city = location["adminArea5"]
        self.postalCode = location["postalCode"]


    def __str__(self):

        return """
            City: {}
            Province/State: {}
            Country: {}
            Postal Code: {}
            """.format(self.city, self.state, self.country, self.postalCode)

    def __eq__(self,other):

        if not isinstance(other, Location):
            return False

        return self.city == other.city and self.province == other.province and self.country == other.country and self.postalCode == other.pastalCode

a = Location("Square One, Mississauga")
print(a)
