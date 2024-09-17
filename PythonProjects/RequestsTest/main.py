import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7217f3c927f71339d0de5dd8adf2c8e4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_pmoncreate = {
    "name": "generate",
    "photo_id": -1
}
body_pmonchange = {
    "pokemon_id": "71416",
    "name": "generate",
    "photo_id": -1
}
body_pmoncatch = {
    "pokemon_id": "71416"
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pmoncreate)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pmonchange)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pmoncatch)
print(response.text)
