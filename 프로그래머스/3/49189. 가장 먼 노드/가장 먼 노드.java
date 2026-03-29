import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        ArrayList<Integer>[] board = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++) {
            board[i] = new ArrayList<>();
        }
        
        int[] dist = new int[n+1];
        Arrays.fill(dist, -1);
        
        for (int[] e: edge) {
            board[e[0]].add(e[1]);
            board[e[1]].add(e[0]);
        }
        
        Queue<Integer> q = new ArrayDeque();
        q.offer(1);
        dist[1] = 0;
        int distance = 0;
        
        while(!q.isEmpty()) {
            int cur = q.poll();
            
            for (int next: board[cur]) {
                if (dist[next] == -1) {
                    dist[next] = dist[cur] + 1;
                    distance = Math.max(distance, dist[next]);
                    q.offer(next);
                }
            }
        }
        
        for (int i = 0; i < n+1; i++) {
            if (distance == dist[i]) {
                answer += 1;
            }
        }
        
        return answer;
    }
}