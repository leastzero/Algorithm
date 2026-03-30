import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        
        Arrays.sort(times);
        
        long lt = times[0];
        long rt = (long) times[times.length-1] * n;
        
        while (lt <= rt) {
            long mid = (lt + rt) / 2;
            
            long people = 0;
            for (int time: times) {
                people += (mid / time);
            }
            
            if (people < n) {
                lt = mid + 1;
            } else {
                answer = mid;
                rt = mid - 1;
            }
        }
        
        return answer;
    }
}