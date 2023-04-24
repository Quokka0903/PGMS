def solution(citations):
    for idx, unit in enumerate(sorted(citations)):
        if unit >= len(citations) - idx:
            return len(citations) - idx