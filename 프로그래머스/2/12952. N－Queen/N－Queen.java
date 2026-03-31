import java.util.*;

class Solution {
    private int[] board;
    private int n;
    private int answer = 0;
    
    public int solution(int n) {
        
        this.n = n;
        this.board = new int[n];
        
        dfs(0);
        
        return answer;
    }
    
    private void dfs(int row) {
        if (row == n) {
            answer++;
            return;
        }
        
        for (int i = 0; i < n; i++) {
            boolean isPossible = true;
            
            for (int j = 0; j < row; j++) {
                if (board[j] == i || Math.abs(row - j) == Math.abs(i - board[j])) {
                    isPossible = false;
                    break;
                }
            }
            
            if (isPossible) {
                board[row] = i;
                dfs(row + 1);
            }
        }
    }
}