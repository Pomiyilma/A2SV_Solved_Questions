class Solution:
    def maxSumBST(self, root):
        self.max_sum = 0
        
        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            left_isBST, left_min, left_max, left_sum = dfs(node.left)
            right_isBST, right_min, right_max, right_sum = dfs(node.right)
            
            if left_isBST and right_isBST and left_max < node.val < right_min:     
                current_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, current_sum)
                return (True, min(left_min, node.val), max(right_max, node.val), current_sum)
        
            else:
                return (False, 0, 0, 0)
        
        dfs(root)
        return self.max_sum
