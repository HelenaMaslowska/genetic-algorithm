# Traveling salesman problem solved by genetic algorithm in Python
[Main](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/main.py) program try to solve problem and show statistics and graphical result shown on plot. Why try? Traveling salesman problem is hard to be solved without using brute force method. Here we use faster solution.
Algorithm is placed [here](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/PMX_algorithm.py). 

## Graph
[Here](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/plot.py) is implemented graph for found solution.

## How it works
PMX choose two segments and replace them. Then, fix all elements which must be unique and check width of this road. The more times this algorithm is repeated, the greater the chance of getting closer to the optimal solution. Here is a mutation which has chance 7% to appear. 

## Mutations
There is 3 types of [mutations](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/mutations.py):
- Swap 2 numbers in input list
- Swap fragment of list
- Get random list started with 0
