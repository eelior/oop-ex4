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
<img src="https://i.ibb.co/Nnsf6kx/showcase-video.gif" alt="logo">


<br/>

## How to Run:

1. The server is a simple .jar file that can be run on any java machine (JDK 11 or above) in a command line, e.g.,  ```java -jar Ex4_Server_v0.0.jar 0```  (where the “0” parameter is a case between [0-15]).
2. Run the ```student_code.py``` file in the same directory as the server.

<br/>

## How it works:

Somewhat similar to the elevators problem, we give each agent his next orders.

So, for each agent in agents we find the next pokemon with the shortest path to and that no other agent is after, and we add it to the list of pokemons to be grabbed.

To implement this, we use a priority queue, which is a data structure that allows us to find the next pokemon with the shortest path to and that no other agent is after. 

For this solution we used our implementation from our previous assignment to shortest path algorithm.

<br/>

## Authors:
- Elior Buskila (@eelior)
- Itamar Casspi (@itamarcasspi)