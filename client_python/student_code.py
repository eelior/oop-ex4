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
from game.Game import Game
from graph.GraphNode import GraphNode
from game.Pokemon import Pokemon

# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = "127.0.0.1"

pygame.init()
try:
    bg = pygame.image.load("../game/sprites/background.jpeg")
except:
    bg = pygame.image.load("game/sprites/background.jpeg")
screen = display.set_mode(
    (WIDTH, HEIGHT), depth=32, flags=HWSURFACE | DOUBLEBUF | RESIZABLE
)
# fake_screen
background = pygame.Surface((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

clock10 = pygame.time.Clock()
time_counter = time.time()
move_counter = 0

FONT = pygame.font.SysFont("Arial", 20, bold=True)

radius = 5

# Colors
black = Color(0, 0, 0)
grey = Color(105, 105, 105)
white = Color(255, 255, 255)
green = Color(81, 255, 13)
yellow = Color(255, 255, 102)

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
    gfxdraw.filled_circle(screen, int(x), int(y), radius, green)
    gfxdraw.aacircle(screen, int(x), int(y), radius, yellow)
    id_srf = FONT.render(str(n1.id), True, black)  # n1 = currNode
    rect = id_srf.get_rect(topright=(x - 10, y - 10))
    screen.blit(id_srf, rect)


def drawEdge(src: GraphNode, dest: GraphNode, color: Color):
    src_x = my_scale(src.pos[0], x=True)
    src_y = my_scale(src.pos[1], y=True)
    dest_x = my_scale(dest.pos[0], x=True)
    dest_y = my_scale(dest.pos[1], y=True)
    pygame.draw.line(screen, color, (src_x, src_y), (dest_x, dest_y), 3)


def is_game_on(client) -> bool:
    try:
        game_running = client.is_running()
    except:
        client.stop_connection()
        sys.exit()
    return game_running


# add agents
for i in range(game.num_of_agents):
    st = "{id:"
    st += str(i)
    st += "}"
    client.add_agent(st)

# this commnad starts the server - the game is running now
client.start()
original_width, original_height = screen.get_width(), screen.get_height()
while is_game_on(client) == "true":
    inf = json.loads(
        client.get_info(), object_hook=lambda d: SimpleNamespace(**d)
    ).GameServer

    # time_delta = clock.tick(60) / 1000.0
    # pokemons
    try:
        game.load_pokemon(client.get_pokemons())
    except:
        client.stop_connection()
        sys.exit()

    try:
        time_to_end = client.time_to_end()
    except:
        client.stop_connection()
        sys.exit()

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
            drawEdge(currNode, dest, green)

    # draw agents
    for agent in game.agents:
        avatar = agent.avatar
        text_rect = avatar.get_rect()
        text_rect.center = (agent.pos[0] - 10, agent.pos[1] + 5)
        agentId = FONT.render(str(agent.id), True, black)
        screen.blit(agentId, text_rect)  # draw agent id
        avatar_rect = avatar.get_rect()
        avatar_rect.center = (agent.pos[0], agent.pos[1])
        screen.blit(avatar, avatar_rect)  # draw agent avatar

    # draw pokemons
    for currPokemon in game.pokemons:
        if currPokemon.type > 0:
            avatar = currPokemon.avatar_bulbasaur
        else:
            avatar = currPokemon.avatar_charmander
        text_rect = avatar.get_rect()
        text_rect.center = (currPokemon.posScale[0] - 35, currPokemon.posScale[1] + 5)
        pokValue = FONT.render(str(currPokemon.value), True, black)
        screen.blit(pokValue, text_rect)  # draw pokemon value
        avatar_rect = avatar.get_rect()
        avatar_rect.center = (currPokemon.posScale[0], currPokemon.posScale[1])
        screen.blit(avatar, avatar_rect)  # draw pokemon avatar

    scale_x = float(screen.get_width()) / original_width
    scale_y = float(screen.get_height()) / original_height
    UI_FONT = pygame.font.SysFont("Arial", int(30 * screen.get_height() / original_height), bold=True)

    info = json.loads(client.get_info())
    timer_clock = UI_FONT.render("Time left:" + time_to_end, True, yellow)
    grade_score = UI_FONT.render("Grade: " + str(info['GameServer']['grade']), True, yellow)
    move_counter = UI_FONT.render("Moves: " + str(info['GameServer']['moves']), True, yellow)
    screen.blit(move_counter, (int(450 * scale_x), 0))
    screen.blit(grade_score, (int(250 * scale_x), 0))
    screen.blit(timer_clock, (0, 0))
    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    game.give_new_orders(client)
    if inf.moves / (time.time() - time_counter) < 10:
        client.move()
# game over:
client.stop_connection()
