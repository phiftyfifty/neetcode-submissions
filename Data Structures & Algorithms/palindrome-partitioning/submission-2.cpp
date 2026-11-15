#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> result;

    vector<vector<string>> partition(string s) {
        vector<string> partitions;
        dfs(s, 0, partitions);
        return this->result;
    }

    void dfs(string& s, int start, vector<string>& subs)
    {
        int n = (int)s.size();

        // If we've reached the end of the string:
        if (start == n)
        {
            this->result.push_back (subs);
            return;
        }

        for (int end = start; end < s.length(); end++)
        {
            if (partition_helper(s, start, end))
            {
                subs.push_back (s.substr(start, end - start + 1));
                dfs(s, end + 1, subs);
                subs.pop_back();
            }
        }
    }

    bool partition_helper(string& s, int left, int right)
    {
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            ++left;
            --right;
        }
        return true;
    }
};
