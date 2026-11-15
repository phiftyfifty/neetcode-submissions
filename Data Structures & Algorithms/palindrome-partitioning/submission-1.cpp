#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<string>> result;

    vector<vector<string>> partition(string s) {
        vector<string> partitions;
        dfs(s, 0, 0, partitions);
        return this->result;
    }

    void dfs(string& s, int j, int i, vector<string>& subs)
    {
        int n = (int)s.size();

        // If we've reached the end of the string:
        if (i == n) {
            // If current chunk also ends exactly at the end, record the path
            if (j == n) {
                this->result.push_back(subs);
            }
            return;
        }

        // Option 1: Cut here if s[j..i] is a palindrome, then start a new piece at i+1
        if (partition_helper(s, j, i)) {
            subs.push_back(s.substr(j, i - j + 1));
            dfs(s, i + 1, i + 1, subs);
            subs.pop_back();
        }

        // Option 2: Don't cut yet; extend the right end
        dfs(s, j, i + 1, subs);
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
