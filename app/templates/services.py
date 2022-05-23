import requests as r 
import random 


class Episode:
    def __init__(self, apidict):
        self.name = apidict['name']
        self.airdate = apidict['air_date']
        self.characters = apidict['characters']
        self.eptag = apidict['episode']
        

def getEpisode():
    data = r.get('https://rickandmortyapi.com/api/episode')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'broken api'

    api_episodes = data['results']
    episodeList = {} 
    for ep in api_episodes:
        new_ep = Episode(ep) 
        episodeList[new_ep.eptag] = new_ep
    return {
        'episodes': episodeList
    }


class Character:
    def __init__(self, imgdict):
        self.name = imgdict['name']
        self.image = imgdict['image']
        self.id = imgdict['id']
        self.status = imgdict['status']
        self.species = imgdict['species']


def getImages():
    data = r.get('https://rickandmortyapi.com/api/character')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'broken api'

    api_char = data['results']
    avatar_imgs= {}
    for char in api_char:
        ea_char = Character(char)
        avatar_imgs[ea_char.name] = ea_char.image
    return {
        'characters': random.choice(list(avatar_imgs.values())),
        'avatars' : random.choice(list(avatar_imgs.values())),
        'another' : random.choice(list(avatar_imgs.values())),  
        'morepics': random.choice(list(avatar_imgs.values())),
        'onemore' : random.choice(list(avatar_imgs.values()))
        }

def getChar():
    data = r.get('https://rickandmortyapi.com/api/character')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'broken api'

    api_char = data['results']
    rm_char= {}
    for char in api_char[:75]:
        ea_char = Character(char)
        rm_char[ea_char.id] = ea_char
    return {
        'all_char': rm_char
    }



