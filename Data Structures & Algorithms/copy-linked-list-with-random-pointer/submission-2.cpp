/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution
{
public:
    unordered_map<Node*, Node*> copy_mp; 
    Node* copyRandomList(Node* head)
    {
        if (!head) return nullptr;
        // recursive approach

        copy_mp[head] = new Node(head->val);
        copy_mp[head->next] = copyRandomList(head->next);
        copy_mp[head]->next = copy_mp[head->next];
        copy_mp[head]->random = copy_mp[head->random];

        return copy_mp[head];
    }
};
