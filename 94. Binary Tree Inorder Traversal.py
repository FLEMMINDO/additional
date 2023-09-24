class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n = TreeNode(1)
l = TreeNode('null')
r = TreeNode(2)
ll = TreeNode(3)
n.left = l
n.right = r
l.left = ll


def inorderTraversal(root):
    ans = []
    route = root
    lcount = 0
    rcount = 0
    while root.left:
        if root.left.val:
            root = root.left
        if route.right.val:
            route = route.right
        ans.append([root.val, route.val])



inorderTraversal(n)



# Input: root = [1,null,2,3]
# Output: [1,3,2]