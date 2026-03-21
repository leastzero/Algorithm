import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        boolean[] visited = new boolean[words.length];
        
        Queue<String> q = new ArrayDeque<>();
        q.offer(begin);
        int level = 0;
        
        while (!q.isEmpty()) {
            int size = q.size();
            
            for (int i = 0; i < size; i++) {
                String cur = q.poll();
                
                if (cur.equals(target)) return level;
                
                for (int j = 0; j < words.length; j++) {
                    if (!visited[j] && canConvert(cur, words[j])) {
                        q.offer(words[j]);
                        visited[j] = true;
                    }
                }
                
            }
            level++;
        }
        
        return 0;
    }
    
    private boolean canConvert(String s1, String s2) {
        int diff = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                diff++;
            }
            if (diff > 1) return false;
        }
        return diff == 1;
    }
}