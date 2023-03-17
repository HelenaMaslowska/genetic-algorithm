# Traveling salesman problem solved by genetic algorithm in Python
[Main](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/main.py) program tries to solve the problem and show statistics and graphical representation shown on a plot. Why try? Traveling salesman problem is hard to solve without using brute force method. Here we use a faster solution.
Algorithm is placed [here](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/PMX_algorithm.py). 

## How it works
PMX chooses two segments and replaces them. Then, it fixes all elements which must be unique and check width of this road. The more times this algorithm is repeated, the greater the chance of getting closer to the optimal solution is. Here is a mutation which has a 7% chance to appear. 

## Graph
[Here](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/plot.py) is an implemented graph for found solution.
<p align="center">
<img src="https://user-images.githubusercontent.com/44245185/220399858-b253945b-842a-443c-b461-745b7c3c2267.png" width=400>
<p>


## Mutations
There are 3 types of [mutations](https://github.com/HelenaMaslowska/genetic-algorithm/blob/main/genetic%20algorithm/mutations.py):
- Swap 2 numbers in input list
- Swap fragment of list
- Get random list started with 0
