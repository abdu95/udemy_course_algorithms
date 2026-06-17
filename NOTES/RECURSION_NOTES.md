

binary search tree using recursion. 
  2
 /  \
1   3
if we delete 2, this is what remains: 
   3
 /   \
1    None

I didnt understand this 




How BST Deletion Works (Conceptually)
When you delete a node in a BST, there are three cases:

    Node has no children (leaf) → Just remove it.
    Node has one child → Replace the node with its child.
    Node has two children → Replace the node with either:
        its in-order successor (the smallest value in its right subtree), or
        its in-order predecessor (the largest value in its left subtree), and then delete that successor/predecessor from its original spot.


successor - voris
predecessor - ajdod


Option A: Use the in-order successor (common approach)

The successor of 2 is the smallest node in its right subtree, which is 3.
Replace 2 with 3.
Then delete 3 from where it originally was (right child of 2). That 3 was a leaf, so it simply disappears.

Resulting tree:

  3
 / \
1  None