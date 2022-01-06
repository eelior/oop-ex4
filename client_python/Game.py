import json

from client_python.GraphAlgo import GraphAlgo


class Game:
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
    def __init__(self, game_info : str):
        """save game info:"""
        load_game = json.loads(game_info)['GameServer']
        self.num_of_pokemon = load_game['pokemons']
        self.login_status = load_game['is_logged_in']
        self.num_of_moves = load_game['moves']
        self.grade = load_game['grade']
        self.game_level = load_game['game_level']
        self.max_user_level = load_game['max_user_level']
        self.id = load_game['id']
        self.num_of_agents = load_game['agents']
        self.pokemons = [] #list of pokemons
        self.agents = [] #list of agents

        """load graph"""
        self.graph = GraphAlgo()
        self.graph.load_from_json(load_game['graph'])

"""
returns: json str of agents. for example:\n
{
    "Agents":[
        {
            "Agent":
            {
                "id":0,
                "value":0.0,
                "src":0,
                "dest":1,
                "speed":1.0,
                "pos":"35.18753053591606,32.10378225882353,0.0"
            }
        }
    ]
}
"""
    # def get_agents(self,agents_info : str) ->bool:
    #     try:
    #         agents_load = json.loads(agents_info)
    #
    #         list_of_agents  = agents_load['Agents']
    #
    #         for i in ListAgents:
    #             ag = a['Agent']
    #             tmp = ag['pos'].split(",")
    #             x = float(tmp[0])
    #             y = float(tmp[1])
    #             pos = (x, y, 0.0)
    #             flag = True
    #             for n in self.agents:
    #                 if n.id == ag['id']:
    #                     n.value = ag['value']
    #                     n.src = ag['src']
    #                     n.dest = ag['dest']
    #                     n.speed = ag['speed']
    #                     n.pos = pos
    #                     flag = False
    #                     break
    #             if flag:
    #                 agent = Agent(ag['id'], ag['value'], ag['src'], ag['dest'], ag['speed'], pos)
    #                 self.agents.append(agent)
    #         return True
    #     except:
    #         return False
    #
    #

