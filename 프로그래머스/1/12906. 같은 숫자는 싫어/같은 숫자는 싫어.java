import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int lastValue = -1;
        
        for (int a: arr) {
            if (lastValue != a) {
                answer.add(a);
                lastValue = a;
            }
        }
        
        int[] ans = new int[answer.size()];
        for (int i = 0; i< answer.size(); i++) {
            ans[i] = answer.get(i);
        }

        return ans;
    }
}