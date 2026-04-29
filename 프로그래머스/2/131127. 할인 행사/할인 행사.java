import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        HashMap<String, Integer> map = new HashMap<>();
        
        int index = 0;
        int day = 10;
        
        for (String w: want) {
            map.put(w, number[index++]);
        }
        
        int n = discount.length - day;
        
        for (int i = 0; i <= n; i++) {
            boolean isRight = true;
            HashMap<String, Integer> bucket = new HashMap<>();
            
            for (int j = i; j < i + day; j++) {
                bucket.put(discount[j], bucket.getOrDefault(discount[j], 0) + 1);
            }
            
            for (String w: want) {
                if (map.get(w) > bucket.getOrDefault(w, 0)) {
                    isRight = false;
                }
            }
            
            if (isRight) answer++;
        }
        
        return answer;
    }
}