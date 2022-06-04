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

# ------------------------------------HOTEL BY LOCATION---------------------------------------#
# HOTEL PARAMS
cityCode = destinationLocationCode
ratings = ["3,4,5"]


# HOTEL SEARCH WITHIN 5KM OF DESTINATION
hotel_info = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city",
                          headers=search_headers, params=f"cityCode={cityCode}&ratings=[4,5]")

hotel_list = hotel_info.json()['data']
hotel_name = [(x['name']) for x in hotel_list]
hotel_id_list = [(x['hotelId']) for x in hotel_list]

# ------------------------------------HOTEL PRICES----------------------------------------------#

# HOTEL PARAMETERS
hotelIds = hotel_id_list
adults = 2
checkInDate = departureDate
checkOutDate = returnDate
priceRange = ""


offer_info = requests.get(url="https://test.api.amadeus.com/v3/shopping/hotel-offers", headers=search_headers,
                          params=f"hotelIds={hotelIds}&adults=2&checkInDate={departureDate}&checkOutDate={returnDate}")

hotel_price_list = offer_info.json()['data']
available_hotels = [(x['hotel']['name']) for x in hotel_price_list]
hotel_prices = [(x['offers'][0]['price']['total']) for x in hotel_price_list]
hotels = {available_hotels[x]: hotel_prices[x] for x in range(len(available_hotels))}

available_hotels_msg = "Of the hotels in the area that match your search criteria, the following have availability\n"\
                       "for your dates (prices in local currency):"
print(available_hotels_msg)
print('\n'.join("{}: {}".format(k, v) for k, v in hotels.items()))
