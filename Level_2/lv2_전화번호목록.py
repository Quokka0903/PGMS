def solution(phone_book):
    answer = True
    phone_book.sort()
    check = phone_book[0]
    for phone in phone_book[1:]:
        if phone.startswith(check):
            answer = False
            break
        else:
            check = phone
    
    return answer