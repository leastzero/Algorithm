import java.util.*;

class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    public int solution(int[][] game_board, int[][] table) {
        int answer = 0;
        int n = game_board.length;
        
        List<List<int[]>> holes = extract(game_board, 0);
        List<List<int[]>> pieces = extract(table, 1);
        
        boolean[] usedPiece = new boolean[pieces.size()];
        
        for (List<int[]> hole: holes) {
            for (int i = 0; i < pieces.size(); i++) {
                if (usedPiece[i]) continue;
                
                List<int[]> piece = pieces.get(i);
                if (hole.size() != piece.size()) continue;
                
                if (isFit(hole, piece)) {
                    answer += piece.size();
                    usedPiece[i] = true;
                    break;
                }
            }
        }
        return answer;
    }
    
    // 빈 공간과 퍼즐 조각 추출
    private List<List<int[]>> extract(int[][] board, int target) {
        int n = board.length;
        boolean[][] visited = new boolean[n][n];
        List<List<int[]>> shapes = new ArrayList<>();
            
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == target && !visited[i][j]) {
                    shapes.add(bfs(board, visited, i, j, target));
                }
            }
        }
        return shapes;
    }
    
    // bfs
    private List<int[]> bfs(int[][] board, boolean[][] visited, int x, int y, int target) {
        List<int[]> shape = new ArrayList<>();
        Queue<int[]> q = new ArrayDeque<>();
        
        q.offer(new int[]{x, y});
        visited[x][y] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int curX = cur[0];
            int curY = cur[1];
            
            shape.add(new int[]{curX, curY});
            
            for (int i = 0; i < 4; i++) {
                int xx = curX + dx[i];
                int yy = curY + dy[i];
                
                if (0 <= xx & xx < board.length && 0 <= yy && yy < board.length) {
                    if (!visited[xx][yy] && board[xx][yy] == target) {
                        visited[xx][yy] = true;
                        q.offer(new int[]{xx, yy});
                    }
                }
            }
        }
        
        return normalize(shape);
    }
    
    // 모양을 (0, 0) 기점으로 이동 (정규화)
    private List<int[]> normalize(List<int[]> shape) {
        int minX = Integer.MAX_VALUE;
        int minY = Integer.MAX_VALUE;
        for (int[] s: shape) {
            minX = Math.min(minX, s[0]);
            minY = Math.min(minY, s[1]);
        }
        
        for (int[] s: shape) {
            s[0] -= minX;
            s[1] -= minY;
        }
        
        shape.sort((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        return shape;
    }
    
    // 빈 공간과 퍼즐 조각이 딱 맞는지 확인
    private boolean isFit(List<int[]> hole, List<int[]> piece) {
        for (int i = 0; i < 4; i++) {
            if (isSame(hole, piece)) return true;
            piece = rotate(piece);
        }
        return false;
    }
    
    // 퍼즐 조각 회전
    private List<int[]> rotate(List<int[]> shape) {
        List<int[]> rotated = new ArrayList<>();
        for (int[] s: shape) {
            rotated.add(new int[]{s[1], -s[0]});
        }
        return normalize(rotated);
    }
    
    // 같은지 확인
    private boolean isSame(List<int[]> s1, List<int[]> s2) {
        for (int i = 0; i < s1.size(); i++) {
            if (s1.get(i)[0] != s2.get(i)[0] || s1.get(i)[1] != s2.get(i)[1]) {
                return false;
            }
        }
        return true;
    }
}