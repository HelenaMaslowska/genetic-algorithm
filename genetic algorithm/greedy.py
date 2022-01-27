def greedy_alg(matrix):
    cities_count = len(matrix)
    visited = [0]
    last = visited[len(visited) - 1]
    min = -1
    for _ in range(cities_count - 1):
        for i in range(cities_count):
            if (i not in visited) and ((min == -1) or (matrix[last][i] > 0 and matrix[last][i] < min)):
                min = matrix[last][i]
                new = i
        visited.append(new)
        last = new
        min = -1

    return visited