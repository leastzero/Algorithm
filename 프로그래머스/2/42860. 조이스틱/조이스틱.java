import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        int n = name.length();
        
        int move = n - 1;
        
        for (int i = 0; i < n; i++) {
            char c = name.charAt(i);
            answer += Math.min(c - 'A', 'Z' - c + 1); // 위쪽, 아래쪽 중 어느 방향으로 가는게 더 최소인지
            
            int next = i + 1;
            while (next < n && name.charAt(next) == 'A') { // 다음 문자가 A라면 그 다음 문자로 바로 이동
                next++;
            }
            
            move = Math.min(move, i * 2 + (n - next)); // 오른쪽으로 가는 경우
            move = Math.min(move, (n - next) * 2 + i); // 왼쪽으로 가는 경우
        }
        
        return answer + move; // 알파벳 변경 값 + 위치 이동 값
    }
}