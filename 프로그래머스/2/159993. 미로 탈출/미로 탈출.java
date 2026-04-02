import java.util.*;

class Solution {
    public int solution(String[] maps) {
        
        int answer = 0;
        
        int sx = 0, sy = 0, ex = 0, ey = 0, lx = 0, ly = 0;
        int n = maps.length;
        int m = maps[0].length();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) == 'S') {
                    sx = i;
                    sy = j;
                }
                if (maps[i].charAt(j) == 'E') {
                    ex = i;
                    ey = j;
                }
                if (maps[i].charAt(j) == 'L') {
                    lx = i;
                    ly = j;
                }
            }
        }
        
        int l_dist = bfs(sx, sy, lx, ly, n, m, maps);
        int e_dist = bfs(lx, ly, ex, ey, n, m, maps);
        
        if (l_dist == -1) return -1;
        if (e_dist == -1) return -1;
        
        answer = l_dist + e_dist;
        
        return answer;
    }
    
    private int bfs(int sx, int sy, int ex, int ey, int n, int m, String[] maps) {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new ArrayDeque<>();
        visited[sx][sy] = true;
        q.offer(new int[]{sx, sy, 0});
        
        while (!q.isEmpty()) {
            int cur[] = q.poll();
            int curX = cur[0];
            int curY = cur[1];
            int cur_dist = cur[2];
            
            if (curX == ex && curY == ey) {
                return cur_dist;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                        visited[nx][ny] = true;
                        q.offer(new int[]{nx, ny, cur_dist + 1});
                    }
                }
            }
        }
        
        return -1;
    }
}