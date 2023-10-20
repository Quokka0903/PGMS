def solution(maps):
    stack = [[0, 0, 1]]
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for i in range(m)] for i in range(n)]
    while stack:
        here_x, here_y, count = stack.pop(0)
        for dir_x, dir_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            dx, dy = here_x + dir_x, here_y + dir_y
            if 0 <= dx < m and 0 <= dy < n and visited[dy][dx] == 0:
                if maps[dy][dx]:
                    if dx == m - 1 and dy == n - 1:
                        return count + 1
                    visited[dy][dx] = 1
                    maps[dy][dx] = count + 1
                    stack.append([dx, dy, count + 1])
        
    return maps[-1][-1] if visited[-1][-1] else -1