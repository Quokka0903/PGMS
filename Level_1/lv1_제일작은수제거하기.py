def solution(arr):
    idx = arr.index(min(arr))
    return arr[:idx] + arr[idx + 1:] or [-1]