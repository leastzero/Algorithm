import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        int n = players.length;
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            map.put(players[i], i);
        }
        
        for (String calling: callings) {
            int index = map.get(calling); // 순위
            String front_player = players[index-1]; // 내 앞 사람
            
            players[index-1] = calling;
            players[index] = front_player;
            
            map.put(calling, index-1);
            map.put(front_player, index);
        }
        
        return players;
    }
}