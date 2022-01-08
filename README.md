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

## Pokemon assignment:

Every iteration we call the function give_new_orders().

The function will iterate over each agent, and assign it the closest pokemon using find_closest_pokemon() function, which returns the edge which the pokemon resides on.

Every time we assign a pokemon for an agent, we mark it as "taken", so that every iteration of give_new_orders() will not assign the same pokemon to two different agents.

Next, we will use the client function choose_next_edge() and we will assign every agent the pokemon which is closest to.

After we finish iterating over all the agents, we will call the function Move().


<br/>

## Authors:
- Elior Buskila (@eelior)
- Itamar Casspi (@itamarcasspi)
