import java.util.*;

class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int index = 0;
        
        int[][] board = new int[rows+1][columns+1];
        int num = 1;
        for (int i = 1; i < rows+1; i++) {
            for (int j = 1; j < columns+1; j++) {
                board[i][j] = num++;
            }
        }
        
        for (int[] query: queries) {
            int x1 = query[0];
            int y1 = query[1];
            int x2 = query[2];
            int y2 = query[3];
            
            int tmp = board[x1][y1];
            int min = tmp;
            
            // 왼쪽 테두리 회전
            for (int i = x1; i < x2; i++) {
                board[i][y1] = board[i+1][y1];
                min = Math.min(min, board[i][y1]);
            }
            
            // 아래쪽 테두리 회전
            for (int i = y1; i < y2; i++) {
                board[x2][i] = board[x2][i+1];
                min = Math.min(min, board[x2][i]);
            }
            
            // 오른쪽 테두리 회전
            for (int i = x2; i > x1; i--) {
                board[i][y2] = board[i-1][y2];
                min = Math.min(min, board[i][y2]);
            }
            
            // 위쪽 테두리 회전
            for (int i = y2; i > y1; i--) {
                board[x1][i] = board[x1][i-1];
                min = Math.min(min, board[x1][i]);
            }
            
            board[x1][y1+1] = tmp;
            
            answer[index++] = min;
        }
        
        return answer;
    }
}