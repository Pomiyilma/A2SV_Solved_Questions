class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            mid = inorder_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        return helper(0, len(inorder) - 1)



    def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
        
            mid = inorder_map[root_val]
            
            root.left = helper(left_idx, mid - 1)
            root.right = helper(mid + 1, right_idx)
            return root
            
        return helper(0, len(inorder) - 1)
