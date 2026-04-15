import java.util.*;

class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    int answer = 0;
    boolean isArrive = false;
    
    public int solution(String[] board) {
        int n = board.length;
        int m = board[0].length();
        
        char[][] game = new char[n][m];
        
        for (int i = 0; i < n; i++) {
            game[i] = board[i].toCharArray();
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (game[i][j] == 'R') {
                    bfs(i, j, game, n, m);
                }
            }
        }
        
        if (!isArrive) return -1;
        
        return answer;
    }
    
    private void bfs(int x, int y, char[][] game, int n, int m) {
        boolean[][] visited = new boolean[n][m];
        Deque<int[]> q = new ArrayDeque<>();
        
        q.offer(new int[]{x, y, 0});
        visited[x][y] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            int cd = cur[2];
            
            for (int i = 0; i < 4; i++) {
                int nx = cx;
                int ny = cy;
                
                // D 만날 때까지 계속 그 방향으로 직진
                while (true) {
                    int tx = nx + dx[i];
                    int ty = ny + dy[i];
                    
                    if (0 > tx || tx >= n || 0 > ty || ty >= m || game[tx][ty] == 'D') {
                        break;
                    }
                    
                    nx = tx;
                    ny = ty;
                }
                
                if (game[nx][ny] == 'G') {
                    isArrive = true;
                    answer = cd + 1;
                    return;
                }
                
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny, cd+1});
                }
            }
        }
    }
}