import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Deque<Integer> answer = new ArrayDeque<>();
        Deque<Integer> days = new ArrayDeque<>();
        
        for (int i = 0; i < progresses.length; i++) {
            int day = 0;
            while (progresses[i] < 100) {
                progresses[i] += speeds[i];
                day += 1;
            }
            days.add(day);
        }
        
        int cur_day = days.poll();
        int count = 1;
        
        while (!days.isEmpty()) {
            int next_day = days.poll();
            
            if (cur_day >= next_day) {
                count++;
            } else {
                answer.add(count);
                count = 1;
                cur_day = next_day;
            }
        }
        
        answer.add(count);
        
        int[] ans = new int[answer.size()];
        int index = 0;
        for (int num: answer) {
            ans[index++] = num;
        }
        
        return ans;
    }
}