def solution(m, n, puddles):
    route = [[1 for i in range(m)] for i in range(n)]
    meter = 1000000007
    
    for puddle_x, puddle_y in puddles:
        route[puddle_y - 1][puddle_x - 1] = 0
        if puddle_y == 1:
            for i in range(puddle_x - 1, m):
                route[puddle_y - 1][i] = 0
        if puddle_x == 1:
            for i in range(puddle_y - 1, n):
                route[i][puddle_x - 1] = 0
        
    
    for x in range(1, n):
        for y in range(1, m):
            
            if route[x][y] > 0:
                route[x][y] = route[x][y-1] + route[x-1][y]
                
    print(route)
    return route[-1][-1] % meter