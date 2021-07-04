'''

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree. The merge rule is
that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input root1                     Input root2         => Output
              1                           2                 3
             /  \                       /  \               / \
            3    2                      1    3            4   5
           /                             \    \          / \   \
          5                               4    7        5   4   7


Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
'''


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# merge trees: We are given two trees and we need to merge them as described above.
# Algorithm: We will use a recursive algorithm. For every node, we will first merge the left subtree and then we will
#            merge the right subtree.
def mergeTrees(root1, root2):
    # allocate the merged node
    node = TreeNode()

    # boundary conditions to end recursion.
    if not root1:
        return root2
    if not root2:
        return root1

    # merge the left subtree
    if root1.left or root2.left:
        node.left = mergeTrees(root1.left, root2.left)
    #merge the right subtree
    if root1.right or root2.right:
        node.right = mergeTrees(root1.right, root2.right)

    # the merged node is sum of the values of corresponding nodes in the trees
    # if either tree does not have a corresponding value then its value is considered zero.
    if root1.val != None:
        if root2.val != None:
            node.val = root1.val + root2.val
        else:
            node.val = root1.val
    else:
        if root2.val != None:
            node.val = root2.val
        else:
            return None
    return node



# Given an input list of values build a binary tree.
# The input list of values are laid out in a breadth first manner
#
# Algorithm: we will use an auxiliary queue data structure to store the siblings in FIFO order.
#           Since the input list has the left sibling first, we will create that first and put it in the aux queue.
#           Next we will do the same for the right sibling.
#           We will loop until we have processed all values queueing nodes from our aux queue.
def buildTree(values):
    if not values or len(values)==0:
        return None
    rootNode = None
    nodes = []
    node = None
    while(len(values)):
        if not node:
            # initial condition
            node = TreeNode(values.pop(0))
        else:
            # process node from top of aux queue (FIFO)
            node = nodes.pop(0)
        # create left sibling
        if len(values):
            node.left = TreeNode(values.pop(0))
            nodes.append(node.left)
        #create right sibling
        if len(values):
            node.right = TreeNode(values.pop(0))
            nodes.append(node.right)
        # first node allocated is the root of the tree
        if not rootNode:
            rootNode = node
    return rootNode

# Given a binary tree create a list of its values such that the values are laid out in breadth first manner.
#
# Algorithm: We will use a recursive approach and an auxiliary global data structure. As we traverse the tree we
#            will store the siblings in our FIFO. We will deque the oldest element and append its value to our values
#            list. The algorithm will terminate when all nodes in our tree have been processed.
nodes = []
def flattenTree(node, values):
    global nodes
    if node:
        # if there is a valid node then it must have a value and we should add it to our list
        values.append(node.val)
    else:
        # there isn't a valid node, some sibling must be missing so store None
        values.append(None)
        return
    # put the current node's children in the FIFO only if either of them exists.
    # this way we keep the flattened list concise.
    if node.left != None or node.right != None:
        nodes.append(node.left)
        nodes.append(node.right)
    #recurse if there are nodes to be processed in our FIFO.
    if len(nodes):
        flattenTree(nodes.pop(0), values)



if __name__ == '__main__':

    # first tree
    rootNode1 = buildTree([1, 2, 3, None, None, 4, 5])
    values1 = []
    flattenTree(rootNode1, values1)
    print(values1)

    # second tree
    rootNode2 = buildTree([1, 2, None, 10, 11, 4, None])
    values2 = []
    flattenTree(rootNode2, values2)
    print(values2)

    #merge trees
    mergedRoot = mergeTrees(rootNode1, rootNode2)
    valuesMerged = []
    flattenTree(mergedRoot, valuesMerged)
    print(valuesMerged)

