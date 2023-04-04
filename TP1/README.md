# IA - GROUP 22

## How to Run

* From the folder FEUP-IA/ run main.py
```
python TP1/src/main.py
```
* You can select AI or Human, when selecting AI it is shown a list of uninformed search methods and heurisct search methods. 
* When you choose the search method you can choose from the provided game difficulties and the heuristics. 
* You can choose which one you'd like and the AI solves the game and shows you the time it took to get to that solution. 

## Code Organization
* The logic of the game is implemented in the file game_state.py
* The search methods are in the file search_methods.py
* The interface code is present in the folder called interface

## Notes
* Our uniform cost algorithm is the same as BFS because our cost is 1
* We removed the DFS from the interface as I could not solve easy games (we have only iterative deepening)