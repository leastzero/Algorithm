import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        // 소요시간 짧은 순으로 정렬
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        
        // 요청 시각이 빠른 순으로 정렬
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        int count = 0;
        int index = 0;
        int totalTime = 0;
        
        while (count < jobs.length) {
            while (index < jobs.length && jobs[index][0] <= totalTime) {
                pq.offer(jobs[index]); // 요청 시각이 진행된 시간보다 작으면 큐에 넣기
                index++;
            }
            
            if (!pq.isEmpty()) {
                int[] cur = pq.poll();
                answer += ((totalTime - cur[0]) + cur[1]); // 반환 시간
                count++;
                totalTime += cur[1]; // 진행 시간 = 이전 진행 시간 + 작업 소요 시간
            } else {
                totalTime = jobs[index][0]; // 진행 시간 = 작업 요청 시간
            }
        }
        
        return answer / jobs.length;
    }
}