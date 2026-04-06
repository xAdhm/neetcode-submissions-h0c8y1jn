class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> seen = new HashMap<>();

        for(int num : nums) {
            if(seen.containsKey(num)) {
                return true;
            }
            seen.put(num, 1);
        }
        return false;
    }
}