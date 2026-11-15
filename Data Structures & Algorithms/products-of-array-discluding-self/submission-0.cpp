class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums)
    {
        vector<int> prefix (nums.size(), 1);
        vector<int> output (nums.size(), 1);

        int p = 1;

        for (int i = 1; i < nums.size(); i++)
        {
            p *= nums[i-1];
            prefix[i] = p;
        }

        p = 1;
        for (int j = nums.size() - 1; j >= 0; j--)
        {
            output[j] = prefix[j] * p;
            p *= nums[j];
        }
        return output;
    }
};
