# Pac3man: Python3 port of Berkeley Pacman

Porting the Berkeley Pacman assignments over to Python 3.

Just the assignment code, but none of the solutions.

My solution code is on a different branch, but that branch is committed to a private Github repo so that students cannot see it. That is not really pertinent information but I wanted to share it because I was really excited to figure it out.

This repo also contains two other assignments, a Markov Babbler and a Naive Bayesian Spam Classifier.
# Maze Search Algorithm Performance

Here are the tables for each maze (tinyMaze, mediumMaze, bigMaze) with the actual time and length of the path for each search algorithm (BFS, DFS, UCS, A*). The data is hypothetical and should be replaced with actual results after running the respective commands.

### tinyMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.00041     | 8              |
| DFS       | 0.00076     | 10              |
| UCS       | 0.00083     | 8              |
| A*        | 0.00061     | 8              |

![tinyMaze](img/tinyMaze.png)
### mediumMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.00419     | 68             |
| DFS       | 0.00226     | 130            |
| UCS       | 0.00900     | 68             |
| A*        | 0.00702     | 68             |
![alt text](mediumMaze.png)
### bigMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.00808     | 210            |
| DFS       | 0.00519     | 210            |
| UCS       | 0.04082     | 210            |
| A*        | 0.03424     | 210            |
![alt text](bigMaze.png)

You can fill in the actual time and length of the path for each algorithm after running the respective commands:

- `python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs`
- `python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs`
- `python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs`
- `python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

- `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`
- `python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs`
- `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`
- `python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

- `python pacman.py -l bigMaze -p SearchAgent -a fn=bfs`
- `python pacman.py -l bigMaze -p SearchAgent -a fn=dfs`
- `python pacman.py -l bigMaze -p SearchAgent -a fn=ucs`
- `python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`