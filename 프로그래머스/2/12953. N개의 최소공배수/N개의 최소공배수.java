import java.util.*;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        
        Arrays.sort(arr);
        
        int max = 0;
        int a = arr[0];
        
        // 두 수의 곱 = 최대 공약수 X 최소 공배수
        // 최소 공배수 = 두 수의 곱 / 최대 공약수
        for (int i = 1; i < arr.length; i++) {
            // 최대 공약수
            int index = 1;
            while (index <= arr[i]) {
                if (a % index == 0 && arr[i] % index == 0) {
                    max = index;
                }
                index++;
            }
            
            // 최소 공배수
            a = (a * arr[i]) / max;
        }
        
        answer = a;
        return answer;
    }
}