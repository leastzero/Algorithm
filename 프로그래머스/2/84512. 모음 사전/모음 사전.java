import java.util.*;

class Solution {
    String[] alpha = {"A", "E", "I", "O", "U"};
    List<String> dic = new ArrayList<>();
    
    public int solution(String word) {
        int answer = 0;
        
        dfs("");
        answer = dic.indexOf(word)+1;
        
        return answer;
    }
    
    public void dfs(String str) {
        if (str.length() > 0) dic.add(str);
        if (str.length() == 5) return;
        
        for (int i = 0; i < 5; i++) {
            dfs(str + alpha[i]);
        }
    }
}