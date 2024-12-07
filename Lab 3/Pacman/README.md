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
| BFS       | 0.000935792922973632     | 8              |
| DFS       | 0.000374078750610351     | 10              |
| UCS       | 0.000876665115356445     | 8              |
| A*        | 0.000432491302490234     | 8              |

![tinyMaze](img/tinyMaze.png)

### mediumMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.00418329238891601     | 68             |
| DFS       | 0.00220990180969238     | 130            |
| UCS       | 0.0105187892913818     | 68             |
| A*        | 0.00715208053588867     | 68             |

![mediumMaze](img/mediumMaze.png)

### bigMaze

| Algorithm | Time (s) | Length of Path |
|-----------|----------|----------------|
| BFS       | 0.00728106498718261    | 210            |
| DFS       | 0.00523591041564941    | 210            |
| UCS       | 0.0429921150207519     | 210            |
| A*        | 0.0344471931457519     | 210            |

![bigMaze](img/bigMaze.png)

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

## tinyMazeSearch Function

Returns a sequence of moves that solves tinyMaze. For any other maze, the sequence of moves will be incorrect, so only use this for tinyMaze.

```python
def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]
```

## depthFirstSearch Function

Search the deepest nodes in the search tree first.

Your search algorithm needs to return a list of actions that reaches the goal. Make sure to implement a graph search algorithm.

To get started, you might want to try some of these simple commands to understand the search problem that is being passed in:

```python
def depthFirstSearch(problem):
    start_time = time.time()
    
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = util.Stack()
    frontier.push((startState, []))
    explored = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            end_time = time.time()
            print(f"DFS Time Performance: {end_time - start_time} seconds")
            return actions

        if state not in explored:
            explored.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in explored:
                    newActions = actions + [action]
                    frontier.push((successor, newActions))

    end_time = time.time()
    print(f"DFS Time Performance: {end_time - start_time} seconds")
    return []
```

## breadthFirstSearch Function

Search the shallowest nodes in the search tree first.

```python
def breadthFirstSearch(problem):
    start_time = time.time()
    
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = util.Queue()
    frontier.push((startState, []))
    explored = set()

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if problem.isGoalState(state):
            end_time = time.time()
            print(f"BFS Time Performance: {end_time - start_time} seconds")
            return actions

        if state not in explored:
            explored.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in explored and successor not in [t[0] for t in frontier.list]:
                    newActions = actions + [action]
                    frontier.push((successor, newActions))

    end_time = time.time()
    print(f"BFS Time Performance: {end_time - start_time} seconds")
    return []
```

## uniformCostSearch Function

Search the node of least total cost first.

```python
def uniformCostSearch(problem):
    from util import PriorityQueue
    start_time = time.time()
    
    fringe = PriorityQueue()
    fringe.push(problem.getStartState(), 0)
    visited = set()
    pathToCurrent = PriorityQueue()
    currState = fringe.pop()
    path = []

    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.add(currState)
            for child, direction, cost in problem.getSuccessors(currState):
                newPath = path + [direction]
                costToGo = problem.getCostOfActions(newPath)
                if child not in visited:
                    fringe.push(child, costToGo)
                    pathToCurrent.push(newPath, costToGo)
        currState = fringe.pop()
        path = pathToCurrent.pop()

    end_time = time.time()
    print(f"UCS Time Performance: {end_time - start_time} seconds")
    return path
```

## nullHeuristic Function

A heuristic function estimates the cost from the current state to the nearest goal in the provided SearchProblem. This heuristic is trivial.

```python
def nullHeuristic(state, problem=None):
    return 0
```

## aStarSearch Function

Search the node that has the lowest combined cost and heuristic first.

```python
def aStarSearch(problem, heuristic=nullHeuristic):
    from util import PriorityQueue
    start_time = time.time()
    
    fringe = PriorityQueue()
    fringe.push(problem.getStartState(), 0)
    visited = set()
    pathToCurrent = PriorityQueue()
    currState = fringe.pop()
    path = []

    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.add(currState)
            for child, direction, cost in problem.getSuccessors(currState):
                newPath = path + [direction]
                costToGo = problem.getCostOfActions(newPath) + heuristic(child, problem)
                if child not in visited:
                    fringe.push(child, costToGo)
                    pathToCurrent.push(newPath, costToGo)
        currState = fringe.pop()
        path = pathToCurrent.pop()

    end_time = time.time()
    print(f"A* Time Performance: {end_time - start_time} seconds")
    return path
```

