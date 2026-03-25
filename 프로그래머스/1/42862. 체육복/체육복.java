import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> lostSet = new HashSet<>();
        Set<Integer> reserveSet = new HashSet();
        
        int answer = 0;
        
        for (int r: reserve) {
            reserveSet.add(r);
        }
        
        for (int l: lost) {
            if (reserveSet.contains(l)) reserveSet.remove(l);
            else lostSet.add(l);
        }
        
        List<Integer> sortedLost = new ArrayList<>(lostSet);
        Collections.sort(sortedLost);
        
        for (int sl: sortedLost) {
            if (reserveSet.contains(sl - 1)) {
                lostSet.remove(sl);
                reserveSet.remove(sl - 1);
            } else if (reserveSet.contains(sl + 1)) {
                lostSet.remove(sl);
                reserveSet.remove(sl + 1);
            }
        }
        
        answer = n - lostSet.size();
        
        return answer;
    }
}