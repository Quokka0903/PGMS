def solution(board, moves):
    queue = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                queue.append(board[i][move - 1])
                board[i][move - 1] = 0
                
                if len(queue) > 1:
                    if queue[-1] == queue[-2]:
                        queue.pop()
                        queue.pop()
                        answer += 2
                break
    return answer