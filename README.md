# OOP_EX4
<img src="client_python/sprites/logo.svg.png" alt="logo">

<br/>
<br/>

## About:
This repository presents the final (last) assignment for the OOP course (CS.Ariel 2021),
In this assignment, we were asked to “put into practice” the main tools covered along the course, in particular, we were expected to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible. The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take (aka walk)  the proper edge to “grab” the pokemon. Our goal is to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max).

## Game Showcase:
<img src="client_python/sprites/logo.svg.png" alt="logo">


## How to Run:

1. The server is a simple .jar file that can be run on any java machine (JDK 11 or above) in a command line, e.g.,  ```java -jar Ex4_Server_v0.0.jar 0```  (where the “0” parameter is a case between [0-15]).
2. Run the ```student_code.py``` file in the same directory as the server.

## Authors:
- Elior Buskila @eelior
- Itamar Casspi @itamarcasspi