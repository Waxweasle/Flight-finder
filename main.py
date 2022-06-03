import requests


API_KEY = "YOUR API KEY HERE"
API_SECRET = "YOUR API SECRET HERE"
HEADERS = {"content-type": "application/x-www-form-urlencoded"}
PARAMS = f"grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}"\
         + "x-www-form-urlencoded"


# GET TOKEN
response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",
                         headers={"Content-Type": "application/x-www-form-urlencoded"},
                         data=f"grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}")

token = response.json()['access_token']


# FLIGHT SEARCH
search_headers = {"authorization": f"Bearer {token}"}

# SEARCH INFO -------------
originLocationCode = input("Enter the 3 digit departing airport IATA code:\n").upper()
destinationLocationCode = input("Enter the 3 digit arrival airport IATA code:\n").upper()
departureDate = input("Enter your DEPARTURE date YYYY-MM-DD:\n")
returnDate = input("Enter your RETURN date YYYY-MM-DD:\n")
travelClass = "ECONOMY"
currencyCode = "GBP"
maxPrice = int(input("Enter your maximum ticket price:\n"))
adults = int(input("Enter number of adults:\n"))
max = 3

# FIND THE CHEAPEST FLIGHT FOR GIVEN SEARCH
# ONE WAY OR RETURN
if returnDate == "N/A":
    flight = requests.get(url=f"https://test.api.amadeus.com/v2/shopping/flight-offers", headers=search_headers,
                          params=f"originLocationCode={originLocationCode}&destinationLocationCode="
                                 f"{destinationLocationCode}&departureDate={departureDate}&"
                                 f"currencyCode=GBP&adults={adults}&max=1")
else:
    flight = requests.get(url=f"https://test.api.amadeus.com/v2/shopping/flight-offers", headers=search_headers,
                          params=f"originLocationCode={originLocationCode}&destinationLocationCode="
                                 f"{destinationLocationCode}&departureDate={departureDate}&"
                                 f"returnDate={returnDate}&currencyCode=GBP&adults={adults}&max=1")

flight_price = (flight.json()['data'][0]['price']['total'])

airline = (flight.json()['dictionaries']['carriers'])
airline = list(airline.values())[0]

msg = f"The cheapest flight from {originLocationCode} to {destinationLocationCode} that we found for your dates is " \
      f"£{flight_price} with {airline}.\n"\
      "Head over to their website to book! "
print(msg)


