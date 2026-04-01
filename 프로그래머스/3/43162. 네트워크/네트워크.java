import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n+1];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, n, computers, visited);
                answer++;
            }
        }
        
        return answer;
    }
    
    private void dfs(int i, int n, int[][] computers, boolean[] visited) {
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            
            if (computers[i][j] == 1 && !visited[j]) {
                visited[j] = true;
                dfs(j, n, computers, visited);
            }
        }
    }
}