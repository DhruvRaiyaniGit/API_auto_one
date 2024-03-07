import requests
import pytest

# checking for the status code 200
def test_get_request():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    # print(response.text)
    # print(response.status_code)
    assert response.status_code == 200
    assert len(response.json()) > 0

# Checking the negative scenario, check for the status code = 404
# def test_get_request_neg():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     # print(response.text)
#     # print(response.status_code)
#     assert response.status_code == 404

# generate token
def test_post_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth",headers=headers ,json=payload)

    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])

def test_post_create_booking():

    payload_create_booking = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post("https://restful-booker.herokuapp.com/booking", headers = headers, json=payload_create_booking)

    print(response.json())
    print(response.headers)
    assert response.status_code == 200



# def test_post_request():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.text)
#     print(response.status_code)
#     assert response.status_code == 200
#
#
# def test_patch_request():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.text)
#     print(response.status_code)
#     assert response.status_code == 200
#
#
# def test_delete_request():
#     response = requests.get("https://restful-booker.herokuapp.com/booking")
#     print(response.text)
#     print(response.status_code)
#     assert response.status_code == 200