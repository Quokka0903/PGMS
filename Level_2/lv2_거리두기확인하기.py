from collections import deque
                    
def solution(places):
    answer = []
    
    def bfs(place, idx):
        q = deque([idx])
        direction = {0: [0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}
        visited = [ [False] * 5 for _ in range(5)]
                
        while q:
            x, y, d = q.popleft()
            visited[x][y] = True
            
            for i in range(4):
                temp_x = x + direction[i][0]
                temp_y = y + direction[i][1]
                temp_d = d + 1
    
                if 0 <= temp_x < 5 and 0 <= temp_y < 5 and not visited[temp_x][temp_y]:
                    visited[temp_x][temp_y] = True
                    
                    if place[temp_x][temp_y] == 'P':
                        if temp_d <= 2:
                            return False
    
                    elif place[temp_x][temp_y] == 'O':
                        if temp_d == 1:
                            q.append([temp_x, temp_y, temp_d])
    
        return True
    
    for place in places:
        check = 1
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    res = bfs(place, [i, j, 0])
                    if not res:
                        check = 0
                        
        answer.append(check)
        
    return answer