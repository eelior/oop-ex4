import json

from numpy import sqrt

from GraphAlgo import GraphAlgo
from Agent import Agent
from Pokemon import Pokemon
import sys


def distance(src_x, src_y, dst_x, dst_y):
    return sqrt((src_x - dst_x) ** 2 + (src_y - dst_y) ** 2)


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

        self.size = self.graphAlgo.graph.v_size()


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
        self.pokemons.clear()

        temp_pokemons = []
        for currPokemon in list_of_pokemon:
            pokemon = currPokemon['Pokemon']
            pos_tuple = pokemon['pos'].split(',')
            poke_pos = (float(pos_tuple[0]), float(pos_tuple[1]), float(pos_tuple[2]))
            new_pokemon = Pokemon(pokemon['value'], pokemon['type'], poke_pos, ++self.size)
            temp_pokemons.append(new_pokemon)
        self.pokemons = temp_pokemons

    def find_poke_location(self, pokemon: Pokemon):
        """returns the src and dest of the edge where the pokemon resides"""
        poke_x = pokemon.pos[0]
        poke_y = pokemon.pos[1]
        for src in self.graphAlgo.graph.src_dst.keys():
            for dst in self.graphAlgo.graph.src_dst.get(src).keys():
                src_x = self.graphAlgo.graph.Nodes.get(src).pos[0]
                src_y = self.graphAlgo.graph.Nodes.get(src).pos[1]

                dst_x = self.graphAlgo.graph.Nodes.get(dst).pos[0]
                dst_y = self.graphAlgo.graph.Nodes.get(dst).pos[1]

                if abs(distance(src_x, src_y, poke_x, poke_y) + distance(poke_x, poke_y, dst_x, dst_y)
                       - distance(src_x, src_y, dst_x, dst_y)) < sys.float_info.epsilon:
                    if pokemon.type < 0:
                        return dst, src

                    return src, dst
