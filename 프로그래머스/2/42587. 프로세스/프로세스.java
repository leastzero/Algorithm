import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Deque<Integer> q = new ArrayDeque<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i = 0; i < priorities.length; i++) {
            q.offer(i);
        }
        
        for (int i = 0; i < priorities.length; i++) {
            pq.offer(priorities[i]);
        }
        
        while (!q.isEmpty()) {
            int curIndex = q.poll();
            
            if (priorities[curIndex] == pq.peek()) {
                answer++;
                pq.poll();
                
                if (curIndex == location) {
                    return answer;
                }
            } else {
                q.offer(curIndex);
            }
        }
        
        return answer;
    }
}