import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int n = order.length;
        int cur_num = 1; // 메인 컨테이너 상자 번호
        int order_num = 0; // 메인 컨테이너 벨트 인덱스
    
        Stack<Integer> stack = new Stack<>();
        
        while (order_num < n) {
            if (cur_num <= n && order[order_num] == cur_num) {
                // 메인 컨테이너 벨트에 있는 경우
                answer++;
                cur_num++;
                order_num++;
            } else if (!stack.isEmpty() && stack.peek() == order[order_num]) {
                // 보조 컨테이너 벨트에 있는 경우
                answer++;
                stack.pop();
                order_num++;
            } else if (cur_num <= n) {
                // 메인에 있는거 보조로 옮기기
                stack.push(cur_num);
                cur_num++;
            } else {
                break;
            }
        }
        
        return answer;
    }
}