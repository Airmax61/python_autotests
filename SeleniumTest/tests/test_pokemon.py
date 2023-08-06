import requests
import pytest

token = '140c910558179d80e576da78f358b147'

def test_status_code():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers', params= {'trainer_id' : 1951})
    assert response.status_code == 200


def test_trainer_name():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers', params= {'trainer_id' : 1951})
    assert response.json()['trainer_name'] == 'Тайлер'