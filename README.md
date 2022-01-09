# OOP_EX4
<img src="game/sprites/logo.svg.png" alt="logo">

<br/>
<br/>

## About:
This repository presents the final (last) assignment for the OOP course (CS.Ariel 2021),
In this assignment, we were asked to “put into practice” the main tools covered along the course, in particular, we were expected to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible. The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take (aka walk)  the proper edge to “grab” the pokemon. Our goal is to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max).

<br/>

## Game Showcase:
### Image
<img src="game/sprites/showcase.png" alt="logo">

<br/>

### Video
![poke](https://user-images.githubusercontent.com/74679553/148662018-f1c857a9-c16a-4f87-90ea-88365f4a5b37.gif)


<br/>

## How to Run:

1. The server is a simple .jar file that can be run on any java machine (JDK 11 or above) in a command line, e.g.,  ```java -jar Ex4_Server_v0.0.jar 0```  (where the “0” parameter is a case between [0-15]).
2. Run the ```student_code.py``` file in the same directory as the server.

<br/>

## Agent's movments:
The goal of the game is for the agents to catch as many pokemons possible.

There are 15 levels in the game where their info is given by the server. Each level determines:

- The number of Pokemon, and the speed which they spawn.
- The number of Agents that spawn at the start of the game.
- The number of nodes and edges of the graph.

The graph is a directed weighted graph, where the weight of each edge determines the speed of every agent that tries to cross it.



In the driver code, student_code class, we will build the GUI and call the functions that play the game. Every iteration we call the function give_new_orders().

The function will iterate over each agent, and assign it the closest pokemon using find_closest_pokemon() function, which returns the edge which the pokemon resides on.

Every time we assign a pokemon for an agent, we mark it as "taken", so that every iteration of give_new_orders() will not assign the same pokemon to two different agents.

Next, we will use the client function choose_next_edge() and we will assign every agent the pokemon which is closest to.

After we finish iterating over all the agents, we will call the function Move().

## Function and class used:

  class Agent:
  
      def __init__(self, id1: int, value: float, src: int, dest: int, speed: float, pos: tuple):

       The class that represents the agents. 
       Holds information such as id, location, speed, sprites etc.

    
class Pokemon:

      def __init__(self, value: float, type: int, pos: tuple):

        The class that represents the Pokemon
        Holds information such as location, weight, type and sprites.

class Game:

      def __init__(self, game_info: str): #constructor.

        The class that represents the current game.
        At initialization we recieve the game info using the method client.get_info(), 
        a function that returns all the meta information about the current level (given to us by the client class).
        Holds the updated list of pokemon and agents, and the graph itself.


      def load_agents(self, agents_info: str):

        Method used to load the updated list of agents. 


      def load_pokemon(self, pokemon_info: str):

        Method used to load the updated list of Pokemon.


      def find_poke_location(self, pokemon: Pokemon):

        Method used to find the edge which the given pokemon resides on.
        Used a simple geomtric equation to find if a point is on a line, but since we are dealing with very small fractions
        we used epsilon to gauge whether the point is close enough to the line or not.

        @return src, dst

        
      def find_closest_pokemon(self, agent: Agent):

        Method used to find the closest Pokemon to a given agent.
        For every pokemon in the game, using the graph's method shortest_path(self, id1: int, id2: int) which is implemented using
        Dijkstra algorithm, we calculate the minimal path cost between the agent location and the pokemon's edge src node, taking into consideration the edge's weight.
        Every pokemon that is assigned, we mark as "taken" so that we wont assign two agents to chase after the same pokemon in the same
        "give_new_orders(self, client)" iteration.

        @return closest_pokemon_src,closest_pokemon_dst


      
      def give_new_orders(self, client):

        Method used to assign every agent it's next move. For every agent we find the closest pokemon, and then orders it to go to the next 
        Node in that path. Telling the agent to go to the desired Node is used with choose_next_edge(self, next_agent_node_json), which is a client method.

        The excecution of every order is used by the move() client method, which is called in the class student_code.
        The method is called after we assign every agent it's order for the next move.
        The move function is called only if the average of number of times which we used "move()" is under 10 per second.


class student_code:
    
        The driver code. This is where we draw the GUI, update our game class using the client method (whih recieve meta information straight from the server).
        Also where we use give_new_orders() method and move() method, which is how we actually play the game.




  


<br/>

## Authors:
- Elior Buskila (@eelior)
- Itamar Casspi (@itamarcasspi)
