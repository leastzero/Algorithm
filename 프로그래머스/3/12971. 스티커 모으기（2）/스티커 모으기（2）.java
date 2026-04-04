import java.util.*;

class Solution {
    public int solution(int sticker[]) {
        int answer = 0;
        
        int n = sticker.length;
        
        if (n == 1) return sticker[0];

        int[] dp = new int[n];
        int[] dp2 = new int[n];
        
        dp[0] = sticker[0];
        dp[1] = sticker[0];
        
        dp2[0] = 0;
        dp2[1] = sticker[1];
        
        for (int i = 2; i <= n - 2; i++) {
            dp[i] = Math.max(dp[i-2] + sticker[i], dp[i-1]);
        }
        
        for (int i = 2; i <= n - 1; i++) {
            dp2[i] = Math.max(dp2[i-2] + sticker[i], dp2[i-1]);
        }
        
        answer = Math.max(dp[n-2], dp2[n-1]);

        return answer;
    }
}