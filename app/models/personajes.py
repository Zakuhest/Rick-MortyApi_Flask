import requests

class Personaje:
    def __init__(self, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

class api:
    def request_api(self, n_page):
        url = "https://rickandmortyapi.com/api/character?page="
        response = requests.get(url + n_page)
        return response.json()