import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];
        
        // 보석 종류 몇 개인지 파악
        Set<String> unique_gems = new HashSet<>();
        for (String gem: gems) {
            unique_gems.add(gem);
        }
        int gems_size = unique_gems.size();
        
        // <보석, 갯수> 저장
        Map<String, Integer> maps = new HashMap<>();
        int start = 0;
        int ans_start = 0, ans_end = 0;
        int min_length = Integer.MAX_VALUE;
        
        for (int end = 0; end < gems.length; end++) {
            // 보석 세기
            maps.put(gems[end], maps.getOrDefault(gems[end], 0) + 1);
            
            while (maps.size() == gems_size) { // 모든 보석이 포함되었다면
                if (end - start < min_length) { // 최소 범위 갱신
                    min_length = end - start;
                    ans_start = start + 1;
                    ans_end = end + 1;
                }
                
                // 시작 위치 옮기기 위해 맨 앞 보석 제거
                maps.put(gems[start], maps.get(gems[start]) - 1);
                
                // 맨 앞 보석을 제거했을 때 0개라면 map에서 완전히 제거 (size 비교를 위해)
                if (maps.get(gems[start]) == 0) {
                    maps.remove(gems[start]);
                }
                
                start++;
            }
        }
        
        answer[0] = ans_start;
        answer[1] = ans_end;
        
        return answer;
    }
}