class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        
        for num in nums:
            current = TreeNode(num)

            while stack and stack[-1].val < num:
                current.left = stack.pop()
            if stack:
                stack[-1].right = current
                
            stack.append(current)
        return stack[0] 
        
