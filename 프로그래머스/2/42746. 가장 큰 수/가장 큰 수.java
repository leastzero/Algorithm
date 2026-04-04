import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        String[] str_num = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            str_num[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(str_num, (a, b) -> (b+a).compareTo(a+b));
        
        if (str_num[0].equals("0")) return "0";
        
        for (String str: str_num) {
            answer += str;
        }
        
        return answer;
    }
}