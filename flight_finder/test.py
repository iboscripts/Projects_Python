import requests

API_KEY = "XA14bJf70cnjstztWcoWceKVGSpOCZZZ"
access_token = "XHn9joHGdsnxQI0NHo0NNTAiJGwL"

def get_cheapest_flight():
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=STN&destinationLocationCode=SAW&departureDate=2024-06-12&returnDate=2024-06-12&adults=2&max=2", headers=headers)
        response.raise_for_status()
        data = response.json()
        cheapest_price = 100000000000000000

        for price in data["data"]:
            total_price = float(price["price"]["total"])
            if total_price < cheapest_price:
                cheapest_price = total_price
                print(cheapest_price)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

get_cheapest_flight()