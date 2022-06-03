# Flight-finder
A program that acts as a search engine by connecting to the Amadeus API to find the user flights that fit their desired search criteria.

## Prerequisites
1. Python 3.0+
2. The requests library

## Amadeus API set up
1. Go to https://developers.amadeus.com/register and register for a free account.
2. Once registered, go to My Self-Service Workspace>Create New App
3. Copy and paste your API key and API secret into the relevant fields in the program 
> API_KEY = 
> API_SECRET =

## How to
1. Run the code and enter desired search citeria as prompted (destination, origin, dates etc)
2. The program will return to you the cheapest flight it can find via the API that matches your parameters.
3. Search parameters can be added / removed as needed and full details can be found in the Amadeus "flight-offers" documentation (https://developers.amadeus.com/self-service/category/air/api-doc/flight-offers-search/api-reference)
4. The API does'nt currently return a link so book directly, so the necessary information is displayed by the program for the user to simply book the flight themselves.

## Future improvements
1. Implementing a hotel search for the duration of the trip.
2. Enable bookings to be carried out directly from the program.
3. Create a user interface for ease of use / user experience.
