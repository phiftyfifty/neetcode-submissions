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
        // O(N) space O(N) time double pass hashmap
        copy_mp[nullptr] = nullptr;
        // Create a map for the deepcopied linked list.

        Node* curr_ptr = head;
        // Iterate over each OG Node.
        // Copy next pointer of OG node to to a new node corresponding next pointer of OG Node.
        // -- same for random pointer.
        while (curr_ptr)
        {

            // has the copy been defined yet? 
            if (copy_mp.find(curr_ptr) == copy_mp.end())
            {
                copy_mp[curr_ptr] = new Node(0);
            }

            copy_mp[curr_ptr]->val = curr_ptr->val;


            // (key: deep copy, value: deep copy)
            // has next been defined yet?
            if (copy_mp.find(curr_ptr->next) == copy_mp.end())
                copy_mp[curr_ptr->next]= new Node(0);
            copy_mp[curr_ptr]->next = copy_mp[curr_ptr->next];

            // has random been created as a copy yet? if not create one
            if (copy_mp.find(curr_ptr->random) == copy_mp.end())
            {
                copy_mp[curr_ptr->random] = new Node(0);
            }
            copy_mp[curr_ptr]->random = copy_mp[curr_ptr->random];
            curr_ptr = curr_ptr->next;
        }

        return copy_mp[head];
    }
};
