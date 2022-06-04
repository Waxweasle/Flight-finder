# Flight-finder
A program that acts as a search engine by connecting to the Amadeus API to find the user flights and hotels that fit their desired search criteria.

## Prerequisites
1. Python 3.0+
2. The requests library

## Amadeus API set up
1. Go to https://developers.amadeus.com/register and register for a free account.
2. Once registered, go to My Self-Service Workspace>Create New App
3. Copy and paste your API key and API secret into the relevant fields in the program
4. Follow the instructions on the site to obtain your personal Token with you api key and api secret 
> API_KEY = 
> 
> API_SECRET =

## How to
### Fight search
1. Run the code and enter desired search citeria as prompted (destination, origin, dates etc)
2. The program will return to you the cheapest flight it can find via the API that matches your parameters.
3. Search parameters can be added / removed as needed and full details can be found in the Amadeus "flight-offers" documentation (https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search/api-reference)
4. The API doesn't currently return a link so book directly, so the necessary information is displayed by the program for the user to simply book the flight themselves.
A successful flight search response will look something like:
```
The cheapest flight from LHR to SYD that we found for your dates is £1268.86 with ETIHAD AIRWAYS.
Head over to their website to book! 
```
### Hotel search
1. Hotels will be retrieved from the city entered in 
> cityCode =
this is the city entered in the flight search by default but can be set to any city
2.Hotel ratings included in the searchh are 3 stars and above.
3. Found hotels will be passed into the following request to retireve pricing
4. The following parameters can be editied for individual use 
```
adults = 2
checkInDate = departureDate
checkOutDate = returnDate
priceRange = ""
```
5. A request will be made to Amadeus API and a successful response of available results will be will be shown as
```
Of the hotels in the area that match your search criteria, the following have availability
for your dates (prices in local currency):
Hotel A: 2415.60
Hotel B: 1364.00
Hotel C: 1080.00
```

## Future improvements
1. Enable bookings to be carried out directly from the program.
2. Create a user interface for ease of use / user experience.
