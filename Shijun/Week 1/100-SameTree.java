/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //Method 1: Recursion method - keep checking every node of the tree
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return (isSameTree(p.right, q.right) && isSameTree(p.left, q.left));
    }
}
