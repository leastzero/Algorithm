import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        
        int[] person1 = {1, 2, 3, 4, 5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] count = {0, 0, 0};
        
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == person1[i % person1.length]) count[0]++;
            if (answers[i] == person2[i % person2.length]) count[1]++;
            if (answers[i] == person3[i % person3.length]) count[2]++;
        }
        
        int maxScore = Math.max(count[0], Math.max(count[1], count[2]));
        
        for (int i = 0; i < 3; i++) {
            if (maxScore == count[i]) {
                answer.add(i);
            }
        }
        
        int[] ans = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            ans[i] = answer.get(i) + 1;
        }
        
        return ans;
    }
}