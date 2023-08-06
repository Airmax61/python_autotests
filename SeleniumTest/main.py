import requests

token = '140c910558179d80e576da78f358b147'

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
    "email": "airmax61@rambler.ru",
    "password": "Iloveqa1"
}, headers = {'Content-Type' : 'application/json'})

print(response.text)'''



'''response_add_pokemon = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print(response_add_pokemon.text)'''

'''response_Change_Pokémon = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "5945",
    "name": "Bolt",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print(response_Change_Pokémon.text)'''


response_add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "5945"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print(response_add_pokeball.text)

