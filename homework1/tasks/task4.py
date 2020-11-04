"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    res, dic = 0, {}
    for n1 in a:
        for n2 in b:
            tmp = n1 + n2
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
    for n1 in c:
        for n2 in d:
            tmp = 0 - (n1 + n2)
            if tmp in dic:
                res += dic[tmp]
    return res
