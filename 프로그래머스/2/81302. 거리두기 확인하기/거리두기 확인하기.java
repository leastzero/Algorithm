import java.util.*;

class Solution {
    char[][] board;
    
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    boolean isDistance;
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        board = new char[5][5];
        int index = 0;
        
        for (String[] place: places) {
            isDistance = true;
            
            for (int i = 0; i < 5; i++) {
                board[i] = place[i].toCharArray();
            }
            
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (board[i][j] == 'P' && isDistance) {
                        bfs(i, j, 0);
                    }
                }
            }
            
            if (isDistance) {
                answer[index++] = 1;
            } else {
                answer[index++] = 0;
            }
        }
        
        return answer;
    }
    
    private void bfs(int x, int y, int distance) {
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y, distance});
        
        boolean[][] visited = new boolean[5][5];
        visited[x][y] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            int cd = cur[2];
            
            if (cd >= 2) continue;
            
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (0 <= nx && nx < 5 && 0 <= ny && ny < 5 && !visited[nx][ny]) {
                    if (board[nx][ny] == 'P') {
                        isDistance = false;
                        return;
                    } else if (board[nx][ny] == 'O') {
                        q.offer(new int[]{nx, ny, cd+1});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
    }
}