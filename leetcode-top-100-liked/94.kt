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
    fun inorderTraversal(root: TreeNode?): List<Int> {
        
        var result = arrayListOf<Int>()
        var dq = ArrayDeque<TreeNode>()

        var cur = root

        while(cur != null || dq.isNotEmpty()){
            while(cur!=null) {
                dq.addLast(cur)
                cur = cur.left
            }

            cur = dq.removeLast()
            result.add(cur.`val`)
            cur = cur.right
        }

        return result
    }
}