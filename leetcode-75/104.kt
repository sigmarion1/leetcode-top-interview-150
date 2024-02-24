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
    fun maxDepth(root: TreeNode?): Int {

        if (root == null) return 0

        var maxVal = 0

        class TreeNodeWithCount(
            var node: TreeNode?,
            var count: Int
        )

        var deque = ArrayDeque<TreeNodeWithCount>()

        deque.addFirst(TreeNodeWithCount(root, 1))

        while (deque.isNotEmpty()) {
            val current = deque.removeLast()

            maxVal = max(maxVal, current.count)

            if(current.node == null) {
                continue
            }

             current.node?.left?.let {
                deque.addFirst(TreeNodeWithCount(it, current.count + 1))
            }
            current.node?.right?.let {
                deque.addFirst(TreeNodeWithCount(it, current.count + 1))
            }
        }

        return maxVal

    }
}