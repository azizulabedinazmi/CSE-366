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
| BFS       | 0.01     | 8              |
| DFS       | 0.01     | 8              |
| UCS       | 0.01     | 8              |
| A*        | 0.01     | 8              |

### mediumMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.05     | 68             |
| DFS       | 0.03     | 130            |
| UCS       | 0.04     | 68             |
| A*        | 0.03     | 68             |

### bigMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.20     | 210            |
| DFS       | 0.15     | 230            |
| UCS       | 0.18     | 210            |
| A*        | 0.17     | 210            |

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