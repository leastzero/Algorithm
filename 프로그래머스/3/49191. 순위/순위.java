import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        
        boolean[][] win = new boolean[n+1][n+1];
        
        // 문제에 주어진 직접적인 결과 계산
        for (int[] result: results) {
            win[result[0]][result[1]] = true;
        }
        
        int answer = 0;
        
        // 간접적인 결과 계산 (A가 B를 이기고 B가 C를 이겼다면, A가 C보다 순위가 높음)
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (win[i][k] && win[k][j]) {
                        win[i][j] = true;
                    }
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            int count = 0;
            for (int j = 1; j <= n; j++) {
                if (win[i][j] || win[j][i]) { // 내가 이긴 사람 + 나를 이긴 사람
                    count++;
                }
            }
            
            if (count == n-1) { // 나 제외 모든 사람과의 경기 결과가 주어졌으면 순위 확정 가능
                answer++;
            }
        }
        
        return answer;
    }
}