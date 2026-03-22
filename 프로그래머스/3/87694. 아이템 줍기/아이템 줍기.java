import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int[][] map = new int[101][101];
        
        for (int[] r : rectangle) {
            int sx = r[0] * 2, sy = r[1] * 2;
            int ex = r[2] * 2, ey = r[3] * 2;
            
            for (int i = sx; i <= ex; i++) {
                for (int j = sy; j <= ey; j++) {
                    if (i > sx && i < ex && j > sy && j < ey) {
                        map[i][j] = -1;
                    } else if (map[i][j] != -1) {
                        map[i][j] = 1;
                    }
                }
            }
        }
        
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{characterX * 2, characterY * 2, 0});
        boolean[][] visited = new boolean[101][101];
        visited[characterX * 2][characterY * 2] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            
            int curX = cur[0];
            int curY = cur[1];
            int dist = cur[2];
            
            if (curX == itemX * 2 && curY == itemY * 2) {
                return dist / 2;
            }
            
            for (int i = 0; i < 4; i++) {
                int xx = curX + dx[i];
                int yy = curY + dy[i];
                
                if (0 <= xx && xx < 101 && 0 <= yy && yy < 101) {
                    if (map[xx][yy] == 1 && !visited[xx][yy]) {
                        visited[xx][yy] = true;
                        q.offer(new int[]{xx, yy, dist+1});
                    }
                }
            }
        }
        
        return 0;
    }
}