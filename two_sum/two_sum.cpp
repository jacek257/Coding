#include vector.h
#include map.h

using namespace std;

vector<int> twoSum(vecotr<int> &nums, int target)
{
    map<int, int> visited;
    vector<int> ans;
    for(int i = 0; i < nums.size(); ++i)
    {
        if(visited.find(nums[i]) != visited.end())
        {
            ans.push_back(visited[nums[i]]);
            ans.push_back(i);
            return ans;
        }
        visited[nums[i]] = i
    }
    return ans;
}
