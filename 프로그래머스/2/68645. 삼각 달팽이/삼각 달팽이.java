import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n * (n+1) / 2];
        
        int[][] triangle = new int[n][n];
        int num = 1;
        int cur_row = -1;
        int cur_col = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++ ){
                if (i % 3 == 0) {
                    cur_row++;
                } else if (i % 3 == 1) {
                    cur_col++;
                } else {
                    cur_col--;
                    cur_row--;
                }
                
                triangle[cur_row][cur_col] = num++;
            }
        }
        
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (triangle[i][j] != 0) {
                    answer[index] = triangle[i][j];
                    index++;
                }
            }
        }
        
        return answer;
    }
}