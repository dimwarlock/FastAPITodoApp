from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'UrithTest'
    assert response.json()['email'] == 'Urith@Nadia.com'
    assert response.json()['first_name'] == 'Urith'
    assert response.json()['last_name'] == 'Feehmr'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '+569 72718813'

def test_change_password_success(test_user):
    response = client.put("/user/password", json={
        "password":"lovenadia", 
        "new_password":"lovelovenadia"
    })

    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={
        "password":"lovenadia-1!!", 
        "new_password":"lovelovenadia"
    })

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on Password change.'}

def test_change_phone_number_success(test_user):
    response = client.put("/user/phone_number", json={"phone_number": "11111111"})
    assert response.status_code == status.HTTP_204_NO_CONTENT