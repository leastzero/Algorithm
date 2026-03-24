import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        List<Integer> w = new ArrayList<>();
        List<Integer> h = new ArrayList<>();
        
        for (int[] size: sizes) {
            Arrays.sort(size);
            
            w.add(size[0]);
            h.add(size[1]);
        }
        
        answer = Collections.max(w) * Collections.max(h);
        
        return answer;
    }
}