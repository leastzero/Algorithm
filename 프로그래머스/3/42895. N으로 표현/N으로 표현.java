import java.util.*;

class Solution {
    public int solution(int N, int number) {
  
        // N을 i개 사용해서 만들 수 있는 숫자 dp에 담기 (중복 제거)
        List<Set<Integer>> dp = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            dp.add(new HashSet<>());
        }
        
        // N을 1개 썼을 때 만들 수 있는 수 = N
        dp.get(1).add(N);
        if (N == number) return 1;
        
        for (int i = 2; i < 9; i++) {
            Set<Integer> set = dp.get(i);
            
            // N을 i번 이어 붙인 것
            int repeat = Integer.parseInt(String.valueOf(N).repeat(i));
            set.add(repeat);
            
            // 이전 단계를 이용해서 사칙연산 수행
            // 예를 들어 4개 사용할 때 경우를 구하고 싶다면
            // 1개 사용 + 3개 사용, 2개 사용 + 2개 사용, 3개 사용 + 1개 사용
            // 이 조합들을 사칙연산 수행한 것을 모두 dp에 넣기
            for (int j = 1; j < i; j++) {
                for (int a: dp.get(j)) {
                    for (int b: dp.get(i - j)) {
                        set.add(a + b);
                        set.add(a - b);
                        set.add(a * b);
                        if (b != 0 ) set.add(a / b);
                    }
                }
            }
            
            // dp에 내가 찾고자 하는 숫자가 들어있으면 즉시 종료
            if (set.contains(number)) return i;
        }
        
        return -1;
    }
}