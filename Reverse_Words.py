# You are given a non-empty string S consisting of N characters. In this problem we consider only strings that consist of lower-case English letters (a−z) and spaces. S can be divided into words by splitting it at the spaces and removing them. We want to reverse every word in S. For example, given S = "we test coders", there are three words: "we", "test" and "coders". Reversing the words gives "ew", "tset" and "sredoc". The goal is to return a string with every word in string S reversed and separated by spaces, so the result in the above example should be "ew tset sredoc". You can assume that if there are K spaces in S then there are exactly K + 1 words. Write a function: def solution(S) that, given a non-empty string S consisting of N characters, returns the reversal of every word of S. For example, given S = "we test coders", the function should return "ew tset sredoc", as explained above. Write an efficient algorithm for the following assumptions: the length of string S is within the range [1..200,000]; string S consists only of lower-case letters (a−z) and spaces. Task idea contributed by Stephen Law of Electrum. 3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters).
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [0..200,000];
# string S is made only of lowercase letters (a−z).


string = 'The week was tough'

def solution(s):
    reversed_string = s[::-1]
    return reversed_string


solution(string)
