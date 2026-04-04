import java.util.*;

class Solution {
    List<int[]>[] graph;

    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        
        graph = new ArrayList[n+1];
        for (int i = 1; i < n+1; i++) graph[i] = new ArrayList<>();
        
        for (int[] f: fares) {
            graph[f[0]].add(new int[]{f[1], f[2]});
            graph[f[1]].add(new int[]{f[0], f[2]});
        }
        
        int[] distS = dijkstra(s, n);
        int[] distA = dijkstra(a, n);
        int[] distB = dijkstra(b, n);
                            
        for (int i = 1; i < n+1; i++) {
            int total = distS[i] + distA[i] + distB[i];
            answer = Math.min(answer, total);
        }
                            
        return answer;
    }
                            
    private int[] dijkstra(int start, int n) {
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[]{start, 0});
        dist[start] = 0;
        
        while (!pq.isEmpty()) {
            int cur[] = pq.poll();
            int cur_node = cur[0];
            int cur_dist = cur[1];
            
            if (cur_dist > dist[cur_node]) continue;
            
            for (int[] next: graph[cur_node]) {
                int next_node = next[0];
                int next_dist = next[1];
                
                int cost = dist[cur_node] + next_dist;
                
                if (cost < dist[next_node]) {
                    dist[next_node] = cost;
                    pq.offer(new int[]{next_node, dist[next_node]});
                }
            }
        }
        
        return dist;
    }
}