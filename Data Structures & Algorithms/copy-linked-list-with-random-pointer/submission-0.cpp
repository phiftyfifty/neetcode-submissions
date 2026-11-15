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
        copy_mp[NULL] = NULL;
        // Create a map for the deepcopied linked list.

        Node* curr_ptr = head;
        // Iterate over each OG Node.
        // Copy next pointer of OG node to to a new node corresponding next pointer of OG Node.
        // -- same for random pointer.
        while (curr_ptr)
        {
            // (key: old, value: copy)
            copy_mp[curr_ptr] = new Node(curr_ptr->val);
            curr_ptr = curr_ptr->next;
        }

        curr_ptr = head;
        while (curr_ptr)
        {
            Node* deepcopy = copy_mp[curr_ptr];
            deepcopy->next = copy_mp[curr_ptr->next];
            deepcopy->random = copy_mp[curr_ptr->random];
            curr_ptr = curr_ptr->next;
        }
        return copy_mp[head];
    }
};
