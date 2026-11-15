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

#include <algorithm>

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder)
    {
        
        if (preorder.empty() || inorder.empty()) return nullptr;  
        auto root = new TreeNode(preorder[0]);
        auto mp = std::find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        vector<int> left_side_preorder (preorder.begin() + 1, preorder.begin() + mp + 1);
        vector<int> right_side_preorder (preorder.begin() + mp + 1, preorder.end());
        vector<int> left_side_inorder (inorder.begin(), inorder.begin() + mp);
        vector<int> right_side_inorder (inorder.begin() + mp + 1, inorder.end());
        root->left = buildTree(left_side_preorder, left_side_inorder);
        root->right = buildTree(right_side_preorder, right_side_inorder);
        return root;
    }
};
