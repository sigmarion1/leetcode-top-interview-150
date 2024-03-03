/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        
        var queue = ArrayDeque<Pair<TreeNode, Int>>()

        if (root == null) {
            return false
        }
        
        queue.add(root to root.`val`)

        while(queue.size > 0) {
        
            var current = queue.removeFirst()
            var currentNode = current.first
            var currentSum = current.second

            if (currentSum == targetSum && currentNode.left == null && currentNode.right == null) {
                return true
            }

            if (currentNode.left != null) {
                queue.add(currentNode.left to currentSum + currentNode.left.`val`)
            }

            if (currentNode.right != null) {
                queue.add(currentNode.right to currentSum + currentNode.right.`val`)
            }
        }
        return false
    }
}