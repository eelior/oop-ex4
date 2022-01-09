import unittest

from game.Agent import Agent
from game.Game import Game
from game.Pokemon import Pokemon
from graph.GraphAlgo import GraphAlgo


class testGame(unittest.TestCase):

    def test_pokemon_find_edge(self):
        json_str = """{"GameServer":{"pokemons":2,"is_logged_in":false,"moves":601,"grade":521,"game_level":1,"max_user_level":-1,"id":0,"graph":"data/A0","agents":1}}
"""
        game = Game(json_str)
        pokemon_a = Pokemon(5,-1,(35.197656770719604, 32.10191878639921, 0.0)) ## on edge 9-->8
        pokemon_b = Pokemon(5,-1,(35.199963710098416, 32.105723673136964, 0.0))#on edge 4-->3
        pokemon_c = Pokemon(5,-1,(35.195224052340706, 32.10575624080796, 0.0))#on edge 3-->2
        pokemon_d = Pokemon(5, -1,(35.19038634163924, 32.10748920705224, 0.0))#on edge 2-->1
        self.assertEqual(game.find_poke_location(pokemon_a),(9,8))
        self.assertEqual(game.find_poke_location(pokemon_b),(4,3))
        self.assertEqual(game.find_poke_location(pokemon_c),(3,2))
        self.assertEqual(game.find_poke_location(pokemon_d),(2,1))

    def test_find_closest_pokemon(self):
        json_str = """{"GameServer":{"pokemons":2,"is_logged_in":false,"moves":601,"grade":521,"game_level":1,"max_user_level":-1,"id":0,"graph":"data/A0","agents":1}}
        """
        game = Game(json_str)
        game.pokemons.clear()
        game.agents.clear()

        pokemon_a = Pokemon(5,-1,(35.197656770719604, 32.10191878639921, 0.0))
        pokemon_b = Pokemon(8,-1,(35.199963710098416, 32.105723673136964, 0.0))
        agent = Agent(0,0,0,-1,1,(51.0, 269.76945244923553, 0.0))

        game.pokemons.append(pokemon_a)
        game.pokemons.append(pokemon_b)
        game.agents.append(agent)

        self.assertEqual(game.find_closest_pokemon(agent),(9,8))

        game.pokemons.clear()
        game.agents.clear()

        pokemon_a = Pokemon(5, -1, (35.19038634163924, 32.10748920705224, 0.0))
        pokemon_b = Pokemon(8, -1, (35.1992728373109, 32.105605979924384, 0.0))
        agent = Agent(0,0,0,-1,1,(291.2837464494914, 536.9654660005624, 0.0))

        game.pokemons.append(pokemon_a)
        game.pokemons.append(pokemon_b)
        game.agents.append(agent)

        self.assertEqual(game.find_closest_pokemon(agent),(2,1))

        game.pokemons.clear()
        game.agents.clear()

        pokemon_a = Pokemon(5, -1, (35.20729662934775, 32.105174281651756, 0.0))
        pokemon_b = Pokemon(8, -1, (35.19606025016497, 32.10559387118773, 0.0))
        agent = Agent(0, 0, 0, -1, 1, (332.4765868886754, 498.4726224778446, 0.0))

        game.pokemons.append(pokemon_a)
        game.pokemons.append(pokemon_b)
        game.agents.append(agent)

        self.assertEqual(game.find_closest_pokemon(agent), (3, 2))

        game.pokemons.clear()
        game.agents.clear()

        pokemon_a = Pokemon(5, -1, (35.18827457014228, 32.10525326329593, 0.0))
        pokemon_b = Pokemon(8, -1, (35.18808155803418, 32.10487166569699, 0.0))
        agent = Agent(0, 0, 0, -1, 1, (50.0, 269.76945244923553, 0.0))

        game.pokemons.append(pokemon_a)
        game.pokemons.append(pokemon_b)
        game.agents.append(agent)

        self.assertEqual(game.find_closest_pokemon(agent), (1, 0))