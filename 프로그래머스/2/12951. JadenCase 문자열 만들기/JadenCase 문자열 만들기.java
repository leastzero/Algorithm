import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        boolean isFirst = true;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                answer += " ";
                isFirst = true;
            } else {
                if (isFirst) {
                    answer += Character.toString(s.charAt(i)).toUpperCase();
                    isFirst = false;
                } else {
                    answer += Character.toString(s.charAt(i)).toLowerCase();
                }
            }
        }
        
        return answer;
    }
}