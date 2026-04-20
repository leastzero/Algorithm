import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        HashMap<Integer, Integer> bucket = new HashMap<>();
        
        for (int t: tangerine) {
            bucket.put(t, bucket.getOrDefault(t, 0) + 1);
        }
        
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(bucket.entrySet());
        
        Collections.sort(list, (a, b) -> b.getValue().compareTo(a.getValue()));
        
        for (Map.Entry<Integer, Integer> l: list) {
            if (k <= 0) break;
            
            k -= l.getValue();
            answer++;
        }
        
        return answer;
    }
}