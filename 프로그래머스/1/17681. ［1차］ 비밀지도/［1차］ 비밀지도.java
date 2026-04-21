import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++) {
            String map = "";
            String binary = Integer.toBinaryString(arr1[i]|arr2[i]);
            
            while (binary.length() != n) {
                binary = "0" + binary;
            }
            
            for (char b: binary.toCharArray()) {
                if (b == '1') {
                    map += "#";
                } else {
                    map += " ";
                }
            }
            
            answer[i] = map;
        }
        
        return answer;
    }
}