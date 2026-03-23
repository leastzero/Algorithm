import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        ArrayList<Integer> answer = new ArrayList<>();
        Queue<Integer> q = new ArrayDeque<>();
        
        for (int price: prices) {
            q.add(price);
        }
        
        while (!q.isEmpty()) {
            int time = 0;
            int cur = q.poll();
            
            for (int curQ: q) {
                time++;
                if (cur > curQ) {
                    break;
                }
            }
            answer.add(time);
        }
        
        int[] ans = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            ans[i] = answer.get(i);
        }
        
        return ans;
    }
}