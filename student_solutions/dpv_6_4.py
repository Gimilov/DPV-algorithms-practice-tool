"""
DPV 6.4:

You are given a string of n characters s[1...n], which you 
believe to be a corrupted text document in which all punctuation 
has vanished (so that it looks something like “itwasthebestoftimes…”). 
You wish to reconstruct the document using a dictionary, which is 
available in the form of a Boolean function dict(⋅): 

for any string w, dict(w) returns true if w is a 
valid word, false otherwise.

(a) Give a dynamic programming algorithm that determines whether 
the string s[⋅] can be reconstituted as a sequence of valid words. 
The running time should be at most O(n^2), assuming calls to dict 
take unit time.

(b) In the event that the string is valid, make your algorithm 
output the corresponding sequence of words.

Note: for practice, focus on b) only.
"""
from typing import List

def solution(args: tuple) -> List[str]:
    # unpack args
    s, dct = args
    
    # Helper function to check if a word is in the dictionary
    def dict_func(word):
        return word in dct
    
    # Your DP and backtracking logic here
    n = len(s)
    if n == 0:
        return []
        
    S = [False] * n 
    bt = [-1] * n

    S[0] = dict_func(s[0])
    if S[0]:
        bt[0] = 0 

    for i in range(1, n):
        # Check if entire substring s[0:i+1] is a word
        if dict_func(s[0:i+1]):
            S[i] = True
            bt[i] = 0  # Word starts at 0
            continue
            
        # Check all possible splits
        for j in range(i):
            if S[j] and dict_func(s[j+1:i+1]):
                S[i] = True
                bt[i] = j+1  # Word starts at j+1
                break
    
    # backtracking - I assume that if the entire string is not valid -> return []
    if not S[n-1]:
        return []

    res = []
    end = n-1
    while end >= 0:
        start = bt[end]
        word = s[start:end+1]
        res.append(word)
        end = start - 1  # Move to end of previous word

    res.reverse()
    return res
