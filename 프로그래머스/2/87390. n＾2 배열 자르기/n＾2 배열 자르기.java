import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int len = (int)(right - left + 1);
        int[] answer = new int[len];
        
        for (int i = 0; i < len; i++) {
            long cur = left + i;
            
            long row = cur / n;
            long col = cur % n;
            
            answer[i] = (int)(Math.max(row, col) + 1);
        }
        
        return answer;
    }
}