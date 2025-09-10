
exercise_details = {
    "6.1": {
        "description": """A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. 
For instance, if S is [5,15,-30,10,-5,40,10], then [15,-30,10] is a contiguous subsequence 
but [5,15,40] is not.

Input: A list of numbers [a_1, a_2, ..., a_n]
Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero)

For the preceding example, the answer would be [10,-5,40,10] with sum 55.

Hint: For each j ∈ {1,2,...,n}, consider contiguous subsequences ending exactly at position j.

Note: output a list, not just the sum.""",
        "user_solution_scaffold": """from typing import List

def solution(input_arr: List[int]) -> List[int]:
    # your solution here
    return []
"""},
    "6.2": {
    "description": """You are going on a long trip. You start at mile post 0. Along the way 
there are n hotels, at mile posts a_1 < a_2 < ... < a_n, where each 
a_i is measured from the starting point. The only places you are 
allowed to stop are at these hotels, but you can choose which of 
the hotels you stop at. You must stop at the final hotel (at distance 
a_n), which is your destination.

You'd ideally like to travel 200 miles a day, but this may not be 
possible (depending on the spacing of the hotels). If you travel 
x miles during a day, the penalty for that day is (200 - x)^2. You 
want to plan your trip so as to minimize the total penalty - that 
is, the sum, over all travel days, of the daily penalties. Give an 
efficient algorithm that determines the optimal sequence of hotels at
which to stop.

Note: output a list without including 0""",
    "user_solution_scaffold": """from typing import List

def solution(hotels: List[int]) -> List[int]:
    # Your DP and backtracking code here
    return [] 
"""},
    "6.3": {
    "description": """Yuckdonald's is considering opening a series of restaurants along 
Quaint Valley Highway (QVH). The n possible locations are along a 
straight line, and the distances of these locations from the start 
of QVH are, in miles and in increasing order, m_1, m_2, ..., m_n. 
The constraints are as follows:

- At each location, Yuckdonald's may open at most one restaurant. 
The expected profit from opening a restaurant at location i is p_i, 
where p_i > 0 and i = 1, 2, ..., n.

- Any two restaurants should be at least k miles apart, where k 
is a positive integer.

Give an efficient algorithm to compute the maximum expected total 
profit subject to the given constraints.""",
    "user_solution_scaffold": """from typing import List

def solution(args: tuple) -> int:
    distances, profits, k = args  # unpack tuple: List[int], List[int], int
    return 6515
"""},
    "6.4": {
    "description": """You are given a string of n characters s[1...n], which you 
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

Note: for practice, focus on b) only.""",
    "user_solution_scaffold": """from typing import List

def solution(args: tuple) -> List[str]:
    # unpack args
    s, dct = args

    # Helper function to check if a word is in the dictionary
    def dict_func(word):
        return word in dct
    
    # Your DP and backtracking logic here
    return []
"""},
    "6.5": {
    "description": """Pebbling a checkerboard. We are given a checkerboard which has 4 rows and n 
columns, and has an integer written in each square. We are also given a set of 2n 
pebbles, and we want to place some or all of these on the checkerboard (each 
pebble can be placed on exactly one square) so as to maximize the sum of the 
integers in the squares that are covered by pebbles. There is one constraint: for a 
placement of pebbles to be legal, no two of them can be on horizontally or 
vertically adjacent squares (diagonal adjacency is fine).

    (a) Determine the number of legal patterns that can occur in any column (in 
    isolation, ignoring the pebbles in adjacent columns) and describe these 
    patterns.

Call two patterns compatible if they can be placed on adjacent columns to form a 
legal placement. Let us consider subproblems consisting of the first k columns  
1 ≤ k ≤ n. Each subproblem can be assigned a type, which is the pattern 
occurring in the last column.

(b) Using the notions of compatibility and type, give an O(n)-time dynamic
programming algorithm for computing an optimal placement.""",
    "user_solution_scaffold": """from typing import List, Tuple

def solution(board: List[List[int]]) -> int:
    # board is a 4 x n 2D list of integers
    # Returns maximum sum achievable
    # Your implementation here
    return 0
"""},
    "6.6": {
        "description": """Let us define a multiplication operation on three symbols a, b, c 
    according to the following table; thus ab = b, ba = c, and so on. 
    Notice that the multiplication operation defined by the table is 
    neither associative nor commutative.

          a  b  c
        a b  b  a
        b c  b  a
        c a  c  c

    Find an efficient algorithm that examines a string of these symbols, 
    say bbbbac, and decides whether or not it is possible to parenthesize 
    the string in such a way that the value of the resulting expression is 
    a. For example, on input bbbbac your algorithm should return yes 
    because ((b(bb))(ba))c = a.""",
        "user_solution_scaffold": """def solution(s: str) -> bool:
    # Multiplication table definition
    mul_table = {
        ('a', 'a'): 'b',
        ('a', 'b'): 'b', 
        ('a', 'c'): 'a',
        ('b', 'a'): 'c',
        ('b', 'b'): 'b',
        ('b', 'c'): 'a',
        ('c', 'a'): 'a',
        ('c', 'b'): 'c',
        ('c', 'c'): 'c'
    }
    # Returns True if string can be parenthesized to yield 'a', else False
    # Your implementation here
    return False
    """},
    "6.7": {
        "description": """A subsequence is palindromic if it is the same whether read 
left to right or right to left. For instance, the sequence 
    [A, C, G, T, G, T, C, A, A, A, A, T, C, G] 
has many palindromic subsequences, including [A, C, G, C, A], 
[A] and [A, A, A, A] (on the other hand, the subsequence [A, C, T] 
is not palindromic). Devise an algorithm that takes a sequence 
x[1...n] and returns the (length of the) longest palindromic 
subsequence. Its running time should be O(n^2).

Note: please return the longest palindromic subsequence, not just the length of it.""",
        "user_solution_scaffold": """def solution(x: str) -> str:
    # Your DP implementation here
    return '6515'
"""},
    "6.8": {
    "description": """Given two strings x = x1x2...xn and y = y1y2...ym, we wish to find the length
of their longest common substring, that is, the largest k for which there are
indices i and j with x_i x_{i+1} ... x_{i+k-1} = y_j y_{j+1} ... y_{j+k-1}. 
Show how to do this in time O(mn).""",
    "user_solution_scaffold": """def solution(args: tuple) -> int:
    x, y = args
    # Your implementation here
    return 0
"""},
    "6.9": {
    "description": """A certain string-processing language offers a primitive operation 
which splits a string into two pieces. Since this operation involves
copying the original string, it takes n units of time for a string of 
length n, regardless of the location of the cut. Suppose, now, that 
you want to break a string into many pieces. The order in which the 
breaks are made can affect the total running time. For example, if 
you want to cut a 20-character string at positions 3 and 10, then 
making the first cut at position 3 incurs a total cost of 20 + 17 = 37, 
while doing position 10 first has a better cost of 20 + 10 = 30.

Give a dynamic programming algorithm that, given the locations of m cuts 
in a string of length n, finds the minimum cost of breaking the string 
into m + 1 pieces.""",
    "user_solution_scaffold": """def solution(args: tuple) -> int:
    # n: length of string
    # cuts: sorted list of cut positions (0 < cut < n)
    # Returns minimum cost
    # Your implementation here
    return 0
"""},
    "6.11": {
    "description": """Given two strings x = x_1x_2...x_n and y = y_1y_2...y_m, we wish 
to find the length of their longest common subsequence, that is, 
the largest k for which there are indices i_1 < i_2 < ... < i_k and 
j_1 < j_2 < ... < j_k with x_i1x_i2...x_ik = y_j1y_j2...y_jk. Show 
how to do this in time O(mn).""",
    "user_solution_scaffold": """def solution(args: tuple) -> int:
    x, y = args
    # Return the length of the longest common subsequence
    return 0
"""},
    "6.17": {
    "description": """Given an unlimited supply of coins of denominations x_1, x_2, ..., x_n, 
we wish to make change for a value v; that is, we wish to find a set 
of coins whose total value is v. This might not be possible: for instance, 
if the denominations are 5 and 10 then we can make change for 15 but not 
for 12. Give an O(nv) dynamic-programming algorithm for the following problem.

Input: x_1, ... , x_n; v

Question: Is it possible to make change for v using coins of denominations 
x_1, ... , x_n?""",
    "user_solution_scaffold": """def solution(args: tuple) -> bool:
    # unpack args
    denominations, v = args
    return false
"""},
    "6.18": {
    "description": """Consider the following variation on the change-making problem (Exercise 6.17):  
you are given denominations x_1, x_2, ..., x_n, and you want to make 
change for a value v, but you are allowed to use each denomination 
at most once. For instance, if the denominations are 1, 5, 10, 20, 
then you can make change for 16 = 1 + 15 and for 31 = 1 + 10 + 20 
but not for 40 (because you can't use 20 twice).  

Input: Positive integers x_1, x_2, ..., x_n; another integer v.  
Output: Can you make change for v, using each denomination x_i at most once?  

Show how to solve this problem in time O(nv).""",
    "user_solution_scaffold": """def solution(args: tuple) -> bool:
    denominations, v = args
    # Your implementation here
    return False
"""},
    "6.19": {
    "description": """Here is yet another variation on the change-making problem (Exercise 6.17).
Given an unlimited supply of coins of denominations x_1, x_2, ..., x_n, 
we wish to make change for a value v using at most k coins; that is, we 
wish to find a set of <= k coins whose total value is v. This might not 
be possible: for instance, if the denominations are 5 and 10 and k = 6, 
then we can make change for 55 but not for 65. Give an efficient 
dynamic-programming algorithm for the following problem.

Input: x_1, ..., x_n; k; v.
Question: Is it possible to make change for v using at most k coins,
of denominations x_1, ..., x_n?""",
    "user_solution_scaffold": """def solution(args: tuple) -> bool:
    denominations, k, v = args
    # Your implementation here
    return False
"""},
    "6.20": {
    "description": """Optimal binary search trees. Suppose we know the frequency with which keywords
occur in programs of a certain language, for instance:

    begin   5%
    do      40%
    else    8%
    end     4%
    if      10%
    then    10%
    while   23%

We want to organize them in a binary search tree, so that the keyword 
in the root is alphabetically bigger than all the keywords in the left 
subtree and smaller than all the keywords in the right subtree (and 
this holds for all nodes).

      end                       do
     /    \\                  /      \\
    do     then          begin       while
   /  \\    /  \\                       / 
begin else if  while                if
                                  /   \\
                                else  then
                                  \\
                                   end

Figure above has a nicely-balanced example on the left. In this case, 
when a keyword is being looked up, the number of comparisons needed 
is at most three: for instance, in finding "while", only the three 
nodes "end", "then", and "while" get examined. But since we know the 
frequency with which keywords are accessed, we can use an even more 
fine-tuned cost function, the average number of comparisons to look 
up a word. For the search tree on the left, it is

    cost = 1(0.04) + 2(0.40 + 0.10) + 3(0.05 + 0.08 + 0.10 + 0.23) = 2.42.

By this measure, the best search tree is the one on the right, which 
has a cost of 2.18.

Give an efficient algorithm for the following task.

Input: n words (in sorted order); frequencies of these words: p_1, p_2, ..., p_n.
Output: The binary search tree of lowest cost (defined above as the
expected number of comparisons in looking up a word).

Note: 
To keep it simple, your solution can just return the cost of the optimal 
tree (float). Optionally, you may return a tuple (cost, tree), where 'tree' 
is a nested tuple representing the BST in the form: 

    (word, left_subtree, right_subtree), 

with None for empty subtrees. Both forms are supported and will be 
correctly tested.""",
    "user_solution_scaffold": """def solution(args: tuple) -> float | tuple:
    words, frequencies = args
    # Your implementation here

    # Option 1: return just the cost
    # return 2.18

    # Option 2: return cost and tree (nested tuples)
    # return (2.18, ("do",  ("begin", None, ("else", None, ("end", None, None))),
    #                       ("while", ("if", None, ("then", None, None)), None)))
    
    return 0.0
"""},
    "6.25": {
    "description": """Consider the following 3-partition problem. Given integers a_1, ..., a_n, 
we want to determine whether it is possible to partition {1, ..., n} 
into three disjoint subsets I, J, K such that:

    ∑_{i ∈ I} a_i = ∑_{j ∈ J} a_j = ∑_{k ∈ K} a_k = (1/3) ∑_{i=1}^n a_i

For example, for input (1, 2, 3, 4, 4, 5, 8) the answer is yes, because 
there is the partition (1, 8), (4, 5), (2, 3, 4). On the other hand, for 
input (2, 2, 3, 5) the answer is no.

Devise and analyze a dynamic programming algorithm for 3-partition 
that runs in time polynomial in n and in ∑_i a_i.""",
    "user_solution_scaffold": """from typing import List
    
def solution(arr: List) -> bool:
    # Returns True if 3-partition is possible, else False
    # Your implementation here
    return False
"""},
    "6.26": {
    "description": """Sequence alignment. When a new gene is discovered, a standard 
approach to understanding its function is to look through a 
database of known genes and find close matches. The closeness 
of two genes is measured by the extent to which they are aligned. 
To formalize this, think of a gene as being a long string over
an alphabet Σ = {A, C, G, T}. Consider two genes (strings) 
x = ATGCC and y = TACGCA. An alignment of x and y is a way of 
matching up these two strings by writing them in columns, for instance:

    -   A   T   -   G   C   C
    T   A   -   C   G   C   A

Here the "-" indicates a "gap". The characters of each string 
must appear in order, and each column must contain a character 
from at least one of the strings. The score of an alignment is 
specified by a scoring matrix δ of size (|Σ| + 1) x (|Σ| + 1), 
where the extra row and column are to accommodate gaps. For 
instance the preceding alignment has the following score:

δ(-, T) + δ(A, A) + δ(T, -) + δ(-, C) + δ(G, G) + δ(C, C) + δ(C, A).

Give a dynamic programming algorithm that takes as input two 
strings x[1...n] and y[1...m] and a scoring matrix δ, and returns
the highest-scoring alignment. The running time should be O(mn).
""",
    "user_solution_scaffold": """def solution(args: tuple) -> tuple:
    x, y, delta = args
    # Input: x:str, y:str, delta:dict
    # Note that delta is a nested dictionary. Where delta['A']['C'] is a score of A to C.
    # Returns: (score, aligned_x, aligned_y)
    # where aligned_x and aligned_y are strings with gaps ('-') inserted
    # Your implementation here
    return (0, "", "")
"""}
}

