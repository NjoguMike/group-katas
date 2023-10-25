# In an even word, each letter occurs an even number of times.
# Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that must be deleted to obtain an even word.
# Examples:
# 1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).
# 2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).


from collections import Counter

def solution(S):
    letter_counts=Counter(S)
    total_deletions=0
    for count in letter_counts.values():
        if count%2==1:
            total_deletions+=1
    return total_deletions

print(solution( "This is hard"))