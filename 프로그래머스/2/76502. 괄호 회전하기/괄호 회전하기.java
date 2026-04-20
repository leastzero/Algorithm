import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int n = s.length();
        
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            boolean isValid = true;
            
            // 올바른 괄호 문자열인지 판단
            for (char c: s.toCharArray()) {
                if (c == '[' || c == '(' || c == '{') {
                    stack.push(c);
                } else {
                    if (stack.isEmpty()) {
                        isValid = false;
                        break;
                    }

                    char t = stack.pop();
                    if (c == ']' && t != '[') {
                        isValid = false;
                        break;
                    }
                    if (c == ')' && t != '(') {
                        isValid = false;
                        break;
                    }
                    if (c == '}' && t != '{') {
                        isValid = false;
                        break;
                    }
                }
            }
            
            if (!stack.isEmpty()) isValid = false;
            
            if (isValid) answer++;
            
            // 회전하기
            s = s.substring(1) + s.charAt(0);
        }
        
        return answer;
    }
}