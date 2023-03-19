import requests

endpoint = "http://localhost:8000/api/products/3/update/"
data = {
    "title": "tokyo manji",
    "price": 10001
}
get_response = requests.put(endpoint, json=data)
print(get_response.status_code)
print(get_response.json())