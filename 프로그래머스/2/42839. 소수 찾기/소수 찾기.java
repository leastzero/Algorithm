import java.util.*;

class Solution {
    public int solution(String numbers) {
        int answer = 0;

        Set<Integer> set = new HashSet<>();
        
        dfs("", numbers, set);
        
        for (int s: set) {
            if (isPrime(s)) {
                answer++;
            }
        }
        
        return answer;
    }
    
    private void dfs(String prefix, String numbers, Set<Integer> set) {
        if (!prefix.equals("")) {
            set.add(Integer.parseInt(prefix));
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            dfs(prefix + numbers.charAt(i), numbers.substring(0, i) + numbers.substring(i + 1), set);
        }
    }
    
    private boolean isPrime(Integer n) {
        if (n < 2) return false;
        
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}