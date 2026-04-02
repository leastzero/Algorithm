import java.util.*;
import java.io.*;

public class Main {
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        List<int[]>[] graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new int[]{v, w});
        }

        int[] result = solution(V, E, K, graph);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            if (result[i] == INF) sb.append("INF\n");
            else sb.append(result[i]).append("\n");
        }
        System.out.print(sb);
    }

    public static int[] solution(int V, int E, int K, List<int[]>[] graph) {
        int[] dist = new int[V + 1];
        Arrays.fill(dist, INF);

        // (현재 노드, 거리) -> 거리순으로 정렬
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        pq.offer(new int[]{K, 0});
        dist[K] = 0;

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
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