import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7217f3c927f71339d0de5dd8adf2c8e4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "5953"

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json() ["data"][0]["id"] == TRAINER_ID
