import java.util.*;

class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    int n = 0;
    int m = 0;
    
    public int solution(int[][] land) {
        int answer = 0;
        
        n = land.length;
        m = land[0].length;
        
        int[][] visited = new int[n][m];
        Map<Integer, Integer> oil = new HashMap<>();
        int number = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] == 0 && land[i][j] == 1) {
                    int size = bfs(i, j, number, visited, land);
                    oil.put(number, size);
                    number++;
                }
            }
        }
        
        for (int j = 0; j < m; j++) {
            int cur_oil = 0;
            Set<Integer> numbers = new HashSet<>();
            
            for (int i = 0; i < n; i++) {
                if (visited[i][j] != 0) {
                    numbers.add(visited[i][j]);
                }
            }
            
            for (int num: numbers) {
                cur_oil += oil.get(num);
            }
            
            answer = Math.max(cur_oil, answer);
        }
        
        return answer;
    }
    
    private int bfs(int x, int y, int number, int[][] visited, int[][] land) {
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        visited[x][y] = number;
        int count = 1;
        
        while (!q.isEmpty()) {
            int cur[] = q.poll();
            int cx = cur[0];
            int cy = cur[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (land[nx][ny] == 1 && visited[nx][ny] == 0) {
                        count++;
                        visited[nx][ny] = number;
                        q.offer(new int[]{nx, ny});
                    }
                }
            }
        }
        
        return count;
    }
}