import requests

endpoint = "http://localhost:8000/api/products/create/"
data = {
    "title" : "Uzumaki",
    "price" : 398.99
}
get_response = requests.post(endpoint,json=data)
print(get_response.status_code)
print(get_response.json())