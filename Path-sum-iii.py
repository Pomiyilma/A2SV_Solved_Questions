from typing import Optional
from collections import Counter

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Notebook starts with 0:1, like empty path before root.
        # count down downward paths in a binary tree that sum to a target value.
        # go down no up.

        prefix = Counter({0: 1})   #{10:1, 5:1, 3:1, 3:1, -2:1...}
        self.count = 0  #holds total paths found
        
        def dfs(node, curr_sum):
            if not node: 
                return
            curr_sum += node.val   #curr_sum = 10, then curr_sum = 10 + 5 = 15

            if curr_sum - targetSum in prefix:   #if 15 - 8 in prefix (7 in pref)
                self.count += prefix[curr_sum - targetSum]  
            prefix[curr_sum] += 1  

            dfs(node.left, curr_sum)   #go dEEp on both sides
            dfs(node.right, curr_sum)

            prefix[curr_sum] -= 1   #BACKTRACKING
        dfs(root, 0)
        return self.count
