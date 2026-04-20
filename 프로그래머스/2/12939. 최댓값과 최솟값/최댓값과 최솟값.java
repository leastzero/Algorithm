import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] strs = s.split(" ");
        int[] nums = new int[strs.length];
        int index = 0;
        
        for (String str: strs) {
            nums[index++] = Integer.parseInt(str);
        }
        
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        
        for (int num: nums) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        
        answer += Integer.toString(min);
        answer += " ";
        answer += Integer.toString(max);
        
        return answer;
    }
}