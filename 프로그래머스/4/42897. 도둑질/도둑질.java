import java.util.*;

class Solution {
    public int solution(int[] money) {
        int answer = 0;
        
        int n = money.length;
        int[] dp1 = new int[n+1]; // 첫번째집 터는 경우
        int[] dp2 = new int[n+1]; // 첫번째집 안터는 경우
        
        dp1[0] = money[0]; // 첫번째집 털음
        dp1[1] = money[0]; // 첫번째집 털면 두번째집 못터니까 최대값 그대로 유지
        dp2[0] = 0; // 첫번째집 안털음
        dp2[1] = money[1]; // 첫번째집 안털면 두번째집 돈을 훔칠 수 있음
        
        // 첫번째집 터는 경우
        for (int i = 2; i < n-1; i++) {
            dp1[i] = Math.max(dp1[i-1], dp1[i-2] + money[i]);
        }
        
        // 첫번째집 안터는 경우
        for (int i = 2; i < n; i++) {
            dp2[i] = Math.max(dp2[i-1], dp2[i-2] + money[i]);
        }
        
        answer = Math.max(dp1[n-2], dp2[n-1]);
        
        return answer;
    }
}