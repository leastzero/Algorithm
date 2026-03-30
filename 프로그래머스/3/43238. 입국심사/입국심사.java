import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        
        Arrays.sort(times);
        
        long lt = times[0]; // 가장 짧게 심사하는 경우
        long rt = (long) times[times.length-1] * n; // 가장 오래 걸리는 심사관이 모든 사람을 다 심사할 경우
        
        while (lt <= rt) {
            long mid = (lt + rt) / 2;
            
            long people = 0; // 주어진 시간동안 심사할 수 있는 총 인원 수
            for (int time: times) {
                people += (mid / time); // 각 심사관이 mid 시간동안 처리할 수 있는 인원 수 합산
            }
            
            if (people < n) { // 검사해야될 인원 수보다 적게 검사할 수 있는 경우엔 시간 늘리기
                lt = mid + 1;
            } else { // 검사해야될 인원 수보다 많이 검사할 수 있는 경우 그 시간 저장해두고 시간 줄여보기
                answer = mid;
                rt = mid - 1;
            }
        }
        
        return answer;
    }
}