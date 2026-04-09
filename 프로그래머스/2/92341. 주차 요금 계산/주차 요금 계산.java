import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        // <차량번호, 주차시간> Map 생성
        Map<String, Integer> total = new TreeMap<>();
        
        // <차량번호, 입차시간> Map 생성
        Map<String, Integer> input = new HashMap<>();
        
        for (String record: records) {
            // records 빈칸으로 문자열 스플릿(" ")하기
            String[] r = record.split(" ");
            
            // IN과 OUT의 시간 형식을 분 형식으로 계산해서 빼기
            // 분 = (시간 * 60 + 분)
            String[] time = r[0].split(":");
            int hour = Integer.parseInt(time[0]);
            int minute = Integer.parseInt(time[1]);
            int m = hour * 60 + minute;
            
            // IN이면 <차량번호, 입차시간> Map에 저장
            if (r[2].equals("IN")) {
                input.put(r[1], m);
            } else { // OUT이면 현재시간 - 입차시간 계산해서 주차시간 Map 수정, 입차시간 Map에서 제거
                int input_time = input.remove(r[1]);
                int total_time = m - input_time;
                total.put(r[1], total.getOrDefault(r[1], 0) + total_time);
            }
        }
        
        // IN만 있고 OUT이 없으면 OUT을 23:59로 설정하고 주차시간 계산
        // 입차시간 Map에 남아있는 경우는 OUT이 없는 경우임
        for (String number: input.keySet()) {
            int out_time = 23 * 60 + 59;
            int input_time = input.get(number);
            int total_time = out_time - input_time;
            total.put(number, total.getOrDefault(number, 0) + total_time);
        }
        
        int[] answer = new int[total.size()];
        int index = 0;
        
        // 주차 시간이 기본 시간(fee[0])보다 크면 기본 요금(fee[1])+시간당 요금
        // 시간당 요금 = Math.ceil(((주차시간-fee[0]) / fee[2]) * fee[3])
        
        // 주차 시간이 기본 시간보다 작으면 기본 요금만
        for (String number: total.keySet()) {
            int total_time = total.get(number);
            
            if (total_time <= fees[0]) {
                answer[index] = fees[1];
            } else {
                answer[index] = (int) Math.ceil((double) (total_time - fees[0]) / fees[2]) * fees[3] + fees[1];
            }
            index++;
        }
        
        
        return answer;
    }
}