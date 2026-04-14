import java.util.*;

class Solution {
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    char[][] board;
    boolean[][] visited;
    List<Integer> answer = new ArrayList<>();
    
    public int[] solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();
        
        board = new char[n][m];
        
        for (int i = 0; i < n; i++) {
            board[i] = maps[i].toCharArray();
        }
        
        visited = new boolean[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && board[i][j] != 'X') {
                    bfs(i, j, visited, board, n, m);
                }
            }
        }
        
        if (answer.isEmpty()) {
            return new int[]{-1};
        }
        
        Collections.sort(answer);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
    
    private void bfs(int x, int y, boolean[][] visited, char[][] board, int n, int m) {
        Deque<int[]> q = new ArrayDeque<>();
        int count = board[x][y] - '0';
        
        q.offer(new int[]{x, y});
        visited[x][y] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny] && board[nx][ny] != 'X') {
                        q.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                        count += board[nx][ny] - '0';
                    }
                }
            }
        }
        
        answer.add(count);
    }
}