import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 1; i < brown; i++) {
            int bh = brown - (i + i);
            int bw = bh / 2;
            int yh = i;
            int yw = bw - 2;
            
            if (yh * yw == yellow) {
                answer.add(yw+2);
                answer.add(yh+2);
                break;
            }
        }
        
        int[] ans = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            ans[i] = answer.get(i);
        }
        
        return ans;
    }
}