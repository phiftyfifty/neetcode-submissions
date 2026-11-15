/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxPathSum(TreeNode* root)
    {
        // bellman ford: 
        // Finding the longest path 
        // For any node a, sum the left node(s) and right node(s)'s path sum.
        // When we do a depth first search, accumulate the sum for this node a. 
        int sum = root->val;
        dfs(root, sum);
        return sum;

    }
private:
    int dfs (TreeNode* root, int& sum)
    {
        if (!root) return 0;

        int left_sum = max (dfs(root->left, sum), 0);
        int right_sum = max (dfs(root->right, sum), 0);

        sum = max (sum, root->val + left_sum + right_sum);
        return root->val + max(left_sum, right_sum);
    }
};
