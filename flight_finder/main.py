from tkinter import *
import requests
from twilio.rest import Client

API_KEY = "XA14bJf70cnjstztWcoWceKVGSpOCZZZ"
access_token = "75BGy9dkGWO10ZKuIkEk9zdj4Jhc"
twilio_auth_token = "5574e9fe06d7b727545bc1b0a12ac55f"
account_sıd = "AC91a86a0af41379ca9899f1fb02f6027a"

def get_cheapest_flight():
    origin = org_loc_entry.get()
    destination = des_loc_entry.get()
    departure_date = dep_date_entry.get()
    date_return = return_date_entry.get()
    adults = number_pass_entry.get()

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={destination}&departureDate={departure_date}&returnDate={date_return}&adults={adults}", headers=headers)
    response.raise_for_status()
    data = response.json()
    #print(data)

    cheapest_price = 100000000000000000

    for price in data["data"]:
        total_price = float(price["price"]["total"])
        if total_price < cheapest_price:
            cheapest_price = total_price
            print(cheapest_price)
            client = Client(account_sıd, twilio_auth_token)
            message = client.messages.create(
                body=f"!!Cheapest flight was found!! from {origin} to {destination} departure at {departure_date} and "
                     f"return back at {date_return} and the cheapest price is {cheapest_price}€",
                from_='+13142701786',
                to='+905377871412'
            )
            print(message.sid)


window = Tk()
window.title("Flight Finder")

canvas = Canvas(width=500, height=600, highlightthickness=0)
img = PhotoImage(file="PLANE.png")
canvas.create_image(300, 300, image=img)
canvas.grid(column=0, row=0, columnspan=2, sticky="nsew")

origin_location = Label(text="Origin Location Code (IATA code): ")
destination_location = Label(text="Destination Location Code (IATA code): ")
dep_date = Label(text="Departure Date (e.g. 2017-12-25): ")
return_date = Label(text="Return Date (e.g. 2017-12-25): ")
number_pass = Label(text="Number of passenger: ")

org_loc_entry = Entry(width=40)
des_loc_entry = Entry(width=40)
dep_date_entry = Entry(width=40)
return_date_entry = Entry(width=40)
number_pass_entry = Entry(width=40)

origin_location.grid(row=1, column=0, sticky="w")
destination_location.grid(row=2, column=0, sticky="w")
dep_date.grid(row=3, column=0, sticky="w")
return_date.grid(row=4, column=0, sticky="w")
number_pass.grid(row=6, column=0, sticky="w")
org_loc_entry.grid(row=1, column=1, sticky="w", columnspan=2)
des_loc_entry.grid(row=2, column=1, sticky="w", columnspan=2)
dep_date_entry.grid(row=3, column=1, sticky="w", columnspan=2)
return_date_entry.grid(row=4, column=1, sticky="w", columnspan=2)
number_pass_entry.grid(row=6, column=1, sticky="w", columnspan=2)

search_button = Button(text="Search", command=get_cheapest_flight)
search_button.grid(row=7, column=0, columnspan=2)

window.mainloop()
