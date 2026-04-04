import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int[] e: edge) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        
        int[] dist = new int[n+1];
        Arrays.fill(dist, -1);
        
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(1);
        dist[1] = 0;
        int distance = 0;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int next: graph[cur]) {
                if (dist[next] == -1) {
                    dist[next] = dist[cur] + 1;
                    q.offer(next);
                    distance = Math.max(distance, dist[next]);
                }
            }
        }
        
        for (int d: dist) {
            if (d == distance) {
                answer++;
            }
        }
        
        return answer;
    }
}