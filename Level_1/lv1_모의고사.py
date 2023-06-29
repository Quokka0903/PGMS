def solution(answers):
    res = []
    score = [0, 0, 0]

    check_a = [1, 2, 3, 4, 5]
    check_b = [2, 1, 2, 3, 2, 4, 2, 5]
    check_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


    for idx, answer in enumerate(answers):
        if check_a[idx % 5] == answer:
            score[0] += 1
        if check_b[idx % 8] == answer:
            score[1] += 1
        if check_c[idx % 10] == answer:
            score[2] += 1

    for i in range(len(score)):
        if score[i] == max(score):
            res.append(i + 1)

    return res