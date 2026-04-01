class Solution:
    def constructFromPrePost(self, preorder, postorder):
        
        post_map = {val: i for i, val in enumerate(postorder)}
        self.pre_idx = 0
        def helper(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            if left == right:
                return root
            left_root_val = preorder[self.pre_idx]
            mid = post_map[left_root_val]
            
            root.left = helper(left, mid)
            root.right = helper(mid + 1, right - 1)
            
            return root
        return helper(0, len(postorder) - 1)
