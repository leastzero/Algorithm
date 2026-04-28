import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        
        HashSet<Integer> set = new HashSet<>();
        for (int i = 1; i <= elements.length; i++) {
            for (int j = 0; j < elements.length; j++) {
                int sum = 0;
                int start = j;
                int end = j + i ;
                
                for (int k = start; k < end; k++) {
                    sum += elements[k % elements.length];
                }
                
                set.add(sum);
            }
            
        }
        
        answer = set.size();
        
        return answer;
    }
}