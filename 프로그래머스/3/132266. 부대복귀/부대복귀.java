import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        
        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }
        
        int[] dist = new int[n+1];
        Arrays.fill(dist, -1);
        
        for (int[] road: roads) {
            graph[road[0]].add(road[1]);
            graph[road[1]].add(road[0]);
        }
        
        bfs(destination, graph, dist);
        
        for (int i = 0; i < sources.length; i++) {
            answer[i] = dist[sources[i]];
        }
        
        return answer;
    }
    
    private void bfs(int start, List<Integer>[] graph, int[] dist) {
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(start);
        dist[start] = 0;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int next: graph[cur]) {
                if (dist[next] == -1) {
                    dist[next] = dist[cur] + 1;
                    q.offer(next);
                }
            }
        }
    }
}