import requests as r 


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
    print(episodeList)
    return {
        'episodes': episodeList
    }