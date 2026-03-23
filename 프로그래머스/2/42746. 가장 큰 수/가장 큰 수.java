import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        
        String[] strNum = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strNum[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(strNum, (a, b) -> {
           return (b + a).compareTo(a + b); 
        });
        
        if (strNum[0].equals("0")) {
            return "0";
        }
        
        StringBuilder answer = new StringBuilder();
        for (String s: strNum) {
            answer.append(s);
        }
        
        return answer.toString();
    }
}