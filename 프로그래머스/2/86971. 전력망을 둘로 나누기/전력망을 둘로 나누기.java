import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        
        boolean[][] matrix = new boolean[n + 1][n + 1];
        
        // 전선 연결하기
        for (int[] wire: wires) {
            matrix[wire[0]][wire[1]] = matrix[wire[1]][wire[0]] = true;
        }
        
        // 모든 전선 하나씩 끊어보고 최소값 구하기
        for (int[] wire: wires) {
            int v1 = wire[0];
            int v2 = wire[1];
            
            matrix[v1][v2] = matrix[v2][v1] = false;
            
            int count = bfs(v1, n, matrix);
            
            int diff = Math.abs(count - (n - count));
            answer = Math.min(diff, answer);
            
            matrix[v1][v2] = matrix[v2][v1] = true;
        }
        
        return answer;
    }
    
    private Integer bfs(Integer v1, Integer n, boolean[][] matrix) {
        boolean[] visited = new boolean[n+1];
        Queue<Integer> q = new ArrayDeque<>();
        
        q.offer(v1);
        visited[v1] = true;
        int count = 1;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int i = 1; i <= n; i++) {
                if (matrix[cur][i] && !visited[i]) {
                    q.offer(i);
                    visited[i] = true;
                    count++;
                }
            }
        }
        return count;
    }
}