import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        int len = works.length;
        int sum = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b.compareTo(a));
        
        for (int work: works) {
            pq.offer(work);
            sum += work;
        }
        
        int avg = sum / len;
        
        while (n != 0) {
            int cur = pq.poll();
            
            if (cur == 0) return 0;
            
            cur -= 1;
            pq.offer(cur);
            n -= 1;
        }
        
        while (!pq.isEmpty()) {
            int cur = pq.poll();
            answer += cur * cur;
        }
        
        return answer;
    }
}