class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> _map = new HashMap<>();
        int[] ret = { -1, -1 };
        for (int pos = 0; pos < nums.length; pos++) {
            if (_map.containsKey(target - nums[pos])) {
                ret[0] = _map.get(target - nums[pos]);
                ret[1] = pos;
                return ret;
            }
            _map.put(nums[pos], pos);
        }
        return ret;
    }
}
