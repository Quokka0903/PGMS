def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0 for i in range(101)] for i in range(101)]
    visited = [[0 for i in range(101)] for i in range(101)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1 * 2, y2 * 2 + 1):
            for j in range(x1 * 2, x2 * 2 + 1):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    
    for x in range(1, 100):
        for y in range(1, 100):
            if maps[y][x] and maps[y+1][x] and maps[y-1][x] and maps[y][x+1]\
            and maps[y][x-1] and maps[y+1][x+1] and maps[y+1][x-1] and \
            maps[y-1][x+1] and maps [y-1][x-1]:
                visited[y][x] = -1
    
    #print(maps)
    #print(visited)
    
    visited[characterY * 2][characterX * 2] = -1
    stack = [[characterX * 2, characterY * 2, 0]]
    while stack:
        x, y, cnt = stack.pop()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 < nx < 101 and 0 < ny < 101:
                if (visited[ny][nx] == 0 or visited[ny][nx] > cnt + 1) and maps[ny][nx] == 1:
                    #print(nx/2, ny/2, cnt + 1)
                    visited[ny][nx] = cnt + 1
                    if ny == itemY*2 and nx == itemX*2:
                        continue
                    stack.append([nx, ny, cnt + 1])
                
            
    return visited[itemY*2][itemX*2]//2