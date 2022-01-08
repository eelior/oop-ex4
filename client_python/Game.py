import json

from GraphAlgo import GraphAlgo
from Agent import Agent
from Pokemon import Pokemon


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

    def __init__(self, game_info: str):
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
        self.pokemons = []  # list of pokemons
        self.agents = []  # list of agents

        """load graph"""
        self.graphAlgo = GraphAlgo()
        self.graphAlgo.load_from_json(load_game['graph'])

    def load_agents(self, agents_info: str):
        """load agents info to Game"""
        agents_load = json.loads(agents_info)

        list_of_agents = agents_load['Agents']
        temp_agents = []
        for agent in list_of_agents:
            pos_tuple = tuple(agent['Agent']['pos'].split(','))
            agent_pos = (float(pos_tuple[0]), float(pos_tuple[1]), float(pos_tuple[2]))

            new_agent = Agent(agent['Agent']['id'], agent['Agent']['value'], agent['Agent']['src'],
                              agent['Agent']['dest'], agent['Agent']['speed'], agent_pos)
            temp_agents.append(new_agent)
        self.agents = temp_agents

    def load_pokemon(self, pokemon_info: str):
        """load pokemon info to Game"""
        pokemon_load = json.loads(pokemon_info)

        list_of_pokemon = pokemon_load['Pokemons']
        temp_pokemons = []
        for poke in list_of_pokemon:
            pos_tuple = poke['Pokemon']['pos'].split(',')
            poke_pos = (float(pos_tuple[0]), float(pos_tuple[1]), float(pos_tuple[2]))
            new_pokemon = Pokemon(poke['Pokemon']['value'], poke['Pokemon']['type'], poke_pos)
            temp_pokemons.append(new_pokemon)
        self.pokemons = temp_pokemons

    def find_poke_location(self, pokemon: Pokemon):
        """returns the src and dest of the edge where the pokemon resides"""
        x3 = pokemon.pos[0]
        y3 = pokemon.pos[1]
        for src in self.graphAlgo.graph.src_dst.keys():
            for dst in self.graphAlgo.graph.src_dst.get(src).keys():
                x1 = self.graphAlgo.graph.Nodes.get(src).pos[0]
                y1 = self.graphAlgo.graph.Nodes.get(src).pos[1]

                x2 = self.graphAlgo.graph.Nodes.get(dst).pos[0]
                y2 = self.graphAlgo.graph.Nodes.get(dst).pos[1]

                if x1 == x2:
                    """the slope is undefined"""
                    if x3 == x2 and (y2 <= y3 <= y1 or y1 <= y3 <= y2):
                        """the pokemon is alligned with the line and between the src and node"""
                        return src, dst
                slope = (y2 - y1) / (x2 - x1)
                """if the pokemon is on the slope"""
                if (y3 - y1) == slope * (x3 - x1):
                    """if the pokemon is between the src and dst"""
                    if (min(x1, x2) <= x3 <= max(x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2)):
                        """the pokemon is on the edge"""
                        return src, dst
