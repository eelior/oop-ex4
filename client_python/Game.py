import json


class Game():
            """
        returns the current game info. for example:\n
        {
            "GameServer":{
                "pokemons":1,
                "is_logged_in":false,
                "moves":1,
                "grade":0,
                "game_level":0,
                "max_user_level":-1,
                "id":0,
                "graph":"data/A0",
                "agents":1
            }
        }
        """
    def __init__(self, info):
        l = json
        # .loads(json_str)['GameServer']

