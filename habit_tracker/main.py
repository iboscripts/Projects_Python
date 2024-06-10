from _datetime import datetime
import requests

token = "cinko1234"
username = "cinko"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=parameters)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"  #https://pixe.la/v1/users/cinko/graphs/cinko12.html
graph_params = {
    "id": "cinko12",
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": token
}
r = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


today = (datetime.now()).strftime("%Y%m%d")
#print(today)
pixel_endpoint = f"{graph_endpoint}/cinko12"
pixel_params = {
    "date": today,
    "quantity": input("How many hours did you code today?"),
}

t = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(t.text)


"""put_endpoint = f"{pixel_endpoint}/{today}"
put_params = {
    "quantity": "5.8", #yazmak istediğimiz sayı
}
p = requests.delete(url=put_endpoint, json=put_params, headers=headers)
print(p.text)"""