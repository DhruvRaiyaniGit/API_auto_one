# Make GET, POST, PUT, PATCH, DELETE and Verify

import requests

def get_req():
    response = requests.get("https://api.zippopotam.us/NZ/0110")
    print(response.text)
    if response.status_code == 200:
        print("TC#1 : Get Request is successful")


for i in range(10):
    get_req()
