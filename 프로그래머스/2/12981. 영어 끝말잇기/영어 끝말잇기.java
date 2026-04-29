import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};

        Stack<String> stack = new Stack<>();
        int index = 1;
        
        for (int i = 0; i < words.length; i++) {
            if (index > n) index = 1;
            
            String word = words[i];
            
            if (stack.isEmpty()) {
                stack.push(word);
            } else {
                if (stack.contains(word)) {
                    answer[0] = index;
                    answer[1] = i / n + 1;
                    break;
                } else {
                    String pre_word = stack.peek();
                    if (pre_word.charAt(pre_word.length()-1) != word.charAt(0)) {
                        answer[0] = index;
                        answer[1] = i / n + 1;
                        break;
                    } else {
                        stack.push(word);
                    }
                }
            }
            
            index++;
        }

        return answer;
    }
}