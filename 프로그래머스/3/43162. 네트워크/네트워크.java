import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        boolean[] visited = new boolean[n];
        Queue<Integer> q = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                
                q.offer(i);
                visited[i] = true;
                
                while (!q.isEmpty()) {
                    int cur = q.poll();
                    
                    for (int j = 0; j < n; j++) {
                        if (computers[cur][j] == 1 && !visited[j]) {
                            visited[j] = true;
                            q.offer(j);
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}