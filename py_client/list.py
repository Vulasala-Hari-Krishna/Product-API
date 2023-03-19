import requests

endpoint = "http://localhost:8000/api/products/list/"
get_response = requests.get(endpoint)
print(get_response.status_code)
print(get_response.json())