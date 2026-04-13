import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        
        Deque<Integer> q1 = new ArrayDeque<>();
        for (int num: queue1) {
            q1.add(num);
        }
        
        Deque<Integer> q2 = new ArrayDeque<>();
        for (int num: queue2) {
            q2.add(num);
        }
        
        long q1_sum = Arrays.stream(queue1).sum();
        long q2_sum = Arrays.stream(queue2).sum();
        
        if ((q1_sum + q2_sum) % 2 != 0) return -1;
        
        long half_sum = (q1_sum + q2_sum) / 2;
        
        while (q1_sum != half_sum) {
            if (answer > queue1.length * 4) {
                return -1;
            }
            
            if (q1_sum > half_sum) {
                int num = q1.poll();
                q1_sum -= num;
                q2.offer(num);
                q2_sum += num;
                answer += 1;
            } else {
                int num = q2.poll();
                q2_sum -= num;
                q1.offer(num);
                q1_sum += num;
                answer += 1;
            }
        }
        
        return answer;
    }
}