import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        // 거리 초기화
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        // 그래프 구성
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        // 도로 정보 그래프에 채우기
        for (int[] r: road) {
            int start = r[0];
            int end = r[1];
            int time = r[2];
            
            graph.get(start).add(new int[]{end, time});
            graph.get(end).add(new int[]{start, time});
        }
        
        // 우선순위큐 초기화
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        pq.offer(new int[]{1, 0}); // 1번 마을부터 시작
        dist[1] = 0;
        
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int cur_village = cur[0];
            int cur_dist = cur[1];
            
            if (cur_dist > K) continue; // K보다 크므로 패스
            
            for (int[] next: graph.get(cur_village)) {
                int next_village = next[0];
                int next_dist = next[1];
                
                int cost = dist[cur_village] + next_dist; // 다음 마을까지 거리
                
                if (cost < dist[next_village] && cost <= K) {
                    dist[next_village] = cost;
                    pq.offer(new int[]{next_village, cost});
                }
            }
        }
        
        for (int d: dist) {
            if (d <= K) {
                answer++;
            }
        }

        return answer;
    }
}