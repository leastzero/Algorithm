import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < bridge_length; i++) {
            q.add(0);
        }
        
        int time = 0;
        int sum = 0;
        int index = 0;
        while (!q.isEmpty()) {
            time++;
            int cur = q.poll();
            sum -= cur;
            
            if (index < truck_weights.length) {
                int nextTruck = truck_weights[index];
                
            if (sum + nextTruck <= weight) {
                q.add(nextTruck);
                sum += nextTruck;
                index++;
            } else {
                q.add(0);
            }
            }
        }
        
        answer = time;
        
        return answer;
    }
}