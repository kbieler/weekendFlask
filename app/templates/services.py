import requests as r 


class Episode:
    def __init__(self, apidict):
        self.name = apidict['name']
        self.airdate = apidict['air_date']
        self.characters = apidict['characters']
        self.eptag = apidict['episode']

class Character:
    def __init__(self, imgdict):
        self.name = imgdict['name']
        self.image = imgdict['image']
        
        


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

def getImages():
    data = r.get('https://rickandmortyapi.com/api/character')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'broken api'

    api_imgs = data['results']
    avatar_imgs= {}
    for char in api_imgs:
        ea_img = Character(char)
        avatar_imgs[ea_img.name] = ea_img.image
    return {
        'characters': avatar_imgs
    }
