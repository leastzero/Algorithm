import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        int zero = 0;
        int round = 0;
        
        while (!s.equals("1")) {
            round++;
            String replace_str = "";
            
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '0') {
                    zero++;
                } else {
                    replace_str += s.charAt(i);
                }
            }
            
            s = Integer.toBinaryString(replace_str.length());
        }
        
        answer[0] = round;
        answer[1] = zero;
        
        return answer;
    }
}