import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        
        boolean[][] visited = new boolean[n][m];
        
        Queue<int[]> q = new ArrayDeque<>();
        
        q.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        
        while (!q.isEmpty()) {
            
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];
            
            if (x == n - 1 && y == m - 1) {
                return dist;
            }
            
            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                
                if (xx >= 0 && yy >= 0 && xx < n && yy < m && !visited[xx][yy] && maps[xx][yy] != 0) {
                    q.add(new int[]{xx, yy, dist+1});
                    visited[xx][yy] = true;
                }
            }
        }
    
        return -1;
    }
}