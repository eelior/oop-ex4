"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import sys
import time
from Game import Game
from GraphNode import GraphNode
from Pokemon import Pokemon

# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = "127.0.0.1"

pygame.init()
bg = pygame.image.load("client_python/background.jpeg")
screen = display.set_mode(
    (WIDTH, HEIGHT), depth=32, flags=HWSURFACE | DOUBLEBUF | RESIZABLE
)
# fake_screen
background = pygame.Surface((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()


client = Client()
client.start_connection(HOST, PORT)

clock10 = pygame.time.Clock() # TODO is it needed?
time_counter = time.time() # TODO is it needed?
move_counter = 0

FONT = pygame.font.SysFont("Arial", 20, bold=True)
radius = 5
black = Color(0, 0, 0)
white = Color(255, 255, 255)

game = Game(client.get_info())
graph = game.graphAlgo.graph

# get data proportions
min_x_id = min(list(graph.Nodes), key=lambda n: graph.Nodes[n].pos[0])
min_y_id = min(list(graph.Nodes), key=lambda n: graph.Nodes[n].pos[1])
max_x_id = max(list(graph.Nodes), key=lambda n: graph.Nodes[n].pos[0])
max_y_id = max(list(graph.Nodes), key=lambda n: graph.Nodes[n].pos[1])

min_x = graph.Nodes[min_x_id].pos[0]
min_y = graph.Nodes[min_y_id].pos[1]
max_x = graph.Nodes[max_x_id].pos[0]
max_y = graph.Nodes[max_y_id].pos[1]


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """

    return ((data - min_data) / (max_data - min_data)) * (
        max_screen - min_screen
    ) + min_screen


# decorate scale with the correct values
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)



def drawNode(n1: GraphNode):
    x = my_scale(float(n1.pos[0]), x=True)
    y = my_scale(float(n1.pos[1]), y=True)
    gfxdraw.filled_circle(screen, int(x), int(y), radius, black)
    gfxdraw.aacircle(screen, int(x), int(y), radius, Color(255, 255, 102))
    id_srf = FONT.render(str(n1.id), True, black) # n1 = currNode
    rect = id_srf.get_rect(topright=(x - 10, y - 10))
    screen.blit(id_srf, rect)


def drawEdge(src: GraphNode, dest: GraphNode, color: Color):
    src_x = my_scale(src.pos[0], x=True)
    src_y = my_scale(src.pos[1], y=True)
    dest_x = my_scale(dest.pos[0], x=True)
    dest_y = my_scale(dest.pos[1], y=True)
    pygame.draw.line(screen, color, (src_x, src_y), (dest_x, dest_y))

def giveAgentsOrders():
    '''
        # give each agent his next orders
            # for agent in agents:
            #    foundPokemon = pokemon[0]
            #    for pokemon in pokemons:
            #       foundPokemon = find nearest pokemon && available
            #    agent.nextOrders = foundPokemon
    '''

    for agent in game.agents:
        if agent.src == agent.lastDest or len(agent.orders) == 0:
            v = -sys.maxsize # fetching the maximum value
            chosen_pokemon = Pokemon(0.0, 0, (0.0, 0.0, 0.0), 0)
            for pokemon in game.pokemons:
                if not pokemon.is_taken:
                    src1, dest1 = game.find_poke_location(pokemon)
                    agent.lastDest = dest1.id
                    if agent.src == src1.id:
                        w, lst = game.graphAlgo.shortest_path(src1.id, dest1.id)
                    elif agent.src == dest1.id:
                        lst = [src1.id, dest1.id]
                        chosen_pokemon = pokemon
                        agent.orderList = lst
                        break
                    else:
                        w, lst = game.graphAlgo.shortest_path(agent.src, src1.id)
                        w = w + game.graphAlgo.shortest_path(src1.id, dest1.id)[0]
                        lst.append(game.graphAlgo.shortest_path(src1, dest1.id)[1])

                    lst.pop(0)
                    if (pokemon.value - w) > v:
                        v = pokemon.value - w
                        chosen_pokemon = pokemon
                        agent.orderList = lst

            chosen_pokemon.took = True


# add agents
for i in range(game.num_of_agents):
    st = "{id:"
    st += str(i)
    st += "}"
    client.add_agent(st)


# this commnad starts the server - the game is running now
client.start()

while client.is_running() == "true":
    inf = json.loads(client.get_info(), object_hook=lambda d: SimpleNamespace(**d)).GameServer
    time_delta = clock.tick(60) / 1000.0

    # pokemons
    game.load_pokemon(client.get_pokemons())
    for pokemon in game.pokemons:
        x, y, _ = pokemon.pos
        x = my_scale(float(x), x=True)
        y = my_scale(float(y), y=True)
        pokemon.posScale = (x, y, 0.0)

    # agents
    game.load_agents(client.get_agents())
    for a in game.agents:
        x, y, _ = a.pos
        x = my_scale(float(x), x=True)
        y = my_scale(float(y), y=True)
        a.pos = (x, y, 0.0)

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(white)
    screen.blit(bg, (0, 0))


    # draw nodes
    for currNode in graph.Nodes.values():
        drawNode(currNode)
        for currEdge in graph.all_out_edges_of_node(currNode.id):
            dest = graph.Nodes.get(currEdge)
            drawEdge(currNode, dest, black)

    # draw agents
    for agent in game.agents:
        avatar = agent.avatar
        rect = avatar.get_rect()
        rect.center = (agent.pos[0], agent.pos[1])
        agentId = FONT.render(str(agent.id), True, black)
        screen.blit(avatar, rect) # draw agent avatar
        screen.blit(agentId, rect) # draw agent id

    # draw pokemons
    for currPokemon in game.pokemons:
        if currPokemon.type > 0:
            avatar = currPokemon.avatar_bulbasaur
        else:
            avatar = currPokemon.avatar_pikachu
        rect = avatar.get_rect()
        rect.center = (currPokemon.posScale[0], currPokemon.posScale[1])
        pokValue = FONT.render(str(currPokemon.value), True, black)
        screen.blit(avatar, rect) # draw pokemon avatar
        screen.blit(pokValue, rect) # draw pokemon vakue

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # giveAgentsOrders()
    print(game.find_poke_location(game.pokemons[0]))
    # [Refactor] choose next edge - go to next order
    for agent in game.agents:
        if agent.dest == -1:

            next_node = (agent.src - 1) % len(graph.Nodes)
            client.choose_next_edge(
                '{"agent_id":'
                + str(agent.id)
                + ', "next_node_id":'
                + str(next_node)
                + "}"
            )
            ttl = client.time_to_end()
            print(ttl, client.get_info())


    client.move()
# game over:




# ===LEFTOVERS===
    # # draw edges
    # for src in graph.src_dst.keys():
    #     for dest in graph.src_dst[src].keys():
    #         # scaled positions
    #         src_x = my_scale(graph.Nodes[src].pos[0], x=True)
    #         src_y = my_scale(graph.Nodes[src].pos[1], y=True)
    #         dest_x = my_scale(graph.Nodes[dest].pos[0], x=True)
    #         dest_y = my_scale(graph.Nodes[dest].pos[1], y=True)

    #         # draw the line
    #         pygame.draw.line(
    #             screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y)
    #         )

    # # draw agents
    # for agent in agents:
    #     pygame.draw.circle(
    #         screen, Color(122, 61, 23), (int(agent.pos.x), int(agent.pos.y)), 10
    #     )
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    # for p in pokemons:
    #     pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)



    # pokemons = json.loads(
    #     client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)
    # ).Pokemons
    # pokemons = [p.Pokemon for p in pokemons]
    # for p in pokemons:
    #     x, y, _ = p.pos.split(",")
    #     p.pos = SimpleNamespace(
    #         x=my_scale(float(x), x=True), y=my_scale(float(y), y=True)
    #     )
    # agents = json.loads(
    #     client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)
    # ).Agents

    # agents = [agent.Agent for agent in agents]
    # for a in agents:
    #     x, y, _ = a.pos.split(",")
    #     a.pos = SimpleNamespace(
    #         x=my_scale(float(x), x=True), y=my_scale(float(y), y=True)
        # )