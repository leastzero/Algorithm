import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        HashMap<Integer, Integer> pockemon = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (pockemon.containsKey(nums[i])) {
                pockemon.put(nums[i], pockemon.get(nums[i]) + 1);
            } else {
                pockemon.put(nums[i], 1);
            }
        }
        
        if (pockemon.size() > nums.length / 2) {
            answer = nums.length / 2;
        } else {
            answer = pockemon.size();
        }
        
        return answer;
    }
}