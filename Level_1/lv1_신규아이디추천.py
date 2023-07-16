import re

def solution(new_id):
    
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    answer = re.sub('\.+', '.', answer)
    answer = re.sub('^[.]|[.]$', '', answer)
    if answer == '': answer ='a'
    answer = answer[:15]
    answer = re.sub('[.]$', '', answer)
    
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer