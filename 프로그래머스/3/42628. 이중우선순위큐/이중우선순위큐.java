import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        
        TreeMap<Integer, Integer> map = new TreeMap<>(); // 숫자, 개수로 저장
        
        for (String operation: operations) {
            String[] op = operation.split(" ");
            String command = op[0];
            int value = Integer.parseInt(op[1]);
            
            if (command.equals("I")) {
                map.put(value, map.getOrDefault(value, 0) + 1);
            } else if (command.equals("D") && !map.isEmpty()) {
                if (value == 1) {
                    int maxNum = map.lastKey(); // 최대값
                    if (map.get(maxNum) == 1) {
                        map.remove(maxNum);
                    } else {
                        map.put(maxNum, map.get(maxNum)-1);    
                    }
                } else {
                    int minNum = map.firstKey(); // 최소값
                    if (map.get(minNum) == 1) {
                        map.remove(minNum);
                    } else {
                        map.put(minNum, map.get(minNum)-1);    
                    }
                }
            }
        }
        
        if (map.isEmpty()) {
            return new int[]{0, 0};
        } else {
            return new int[]{map.lastKey(), map.firstKey()};
        }
    }
}