"""
DPV 6.20:

Optimal binary search trees. Suppose we know the frequency with which keywords
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
     /    \                  /      \
    do     then          begin       while
   /  \    /  \                       / 
begin else if  while                if
                                  /   \
                                else  then
                                  \
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
correctly tested.
"""
def solution(args: tuple) -> float | tuple:
    words, frequencies = args
    n = len(words)

    S = [[0] * n for _ in range(n)]
    bt = [[None] * n for _ in range(n)]

    for i in range(n):
        S[i][i] = frequencies[i]
        bt[i][i] = i

    for s in range(1, n):   
        for i in range(n - s):
            j = i + s
            total = sum(frequencies[i:j+1])
            min_cost = float("inf")
            for k in range(i, j+1):
                left = S[i][k-1] if k > i else 0
                right = S[k+1][j] if k < j else 0
                cur = total + left + right
                if cur < min_cost:
                    min_cost = cur
                    bt[i][j] = k
            S[i][j] = min_cost

    # backtracking 
    def build_tree(i, j):
        if i > j:
            return None
        root_index = bt[i][j]
        left_sub = build_tree(i, root_index-1)
        right_sub = build_tree(root_index+1, j)
        return (words[root_index], left_sub, right_sub)

    # Option 1: return just the cost
    # return S[0][n-1]

    # Option 2: return cost and tree (nested tuples)
    optimal_tree = build_tree(0, n-1)
    print(optimal_tree)
    return (S[0][n-1], optimal_tree)
   