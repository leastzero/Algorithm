import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        // 역순 정렬
        Arrays.sort(citations);
        
        for (int i = 0; i < citations.length / 2; i++) {
            int temp = citations[i];
            citations[i] = citations[citations.length - 1 - i];
            citations[citations.length - 1 - i] = temp;
        }
        
        
        // H-Index 찾기
        for (int i = 0; i < citations.length; i++) {
            int count = i + 1;
            
            if (count <= citations[i]) {
                answer = count;
            } else {
                break;
            }
        }
        
        return answer;
    }
}