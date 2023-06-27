def solution(participant, completion):
    answer = ''
    players = {}
    for player in completion:
        if player not in players:
            players[player] = 1
        else:
            players[player] += 1
            
    for winner in participant:
        if winner not in players or (players[winner] <= 0):
            answer += winner
            break
        else:
            players[winner] -= 1
        
    return answer