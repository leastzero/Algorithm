import java.util.*;

class Solution {
    String[] answer = {};
    List<String> path = new ArrayList<>();
    boolean found = false;
    
    public String[] solution(String[][] tickets) {
        Arrays.sort(tickets, (a, b) -> a[1].compareTo(b[1])); // 알파벳 순서로 정렬
        
        boolean[] visited = new boolean[tickets.length]; // 티켓 사용 여부
        
        path.add("ICN");
        dfs("ICN", tickets, visited, 0);
        
        return answer;
    }
    
    private void dfs(String cur, String[][] tickets, boolean[] visited, int depth) {
        if (found) return; // 알파벳 정렬을 했으므로 최초로 티켓을 다 사용한 경우가 정답
        
        if (depth == tickets.length) {
            answer = path.toArray(new String[0]); // 리스트를 배열로 변환
            found = true;
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0].equals(cur)) {
                visited[i] = true;
                path.add(tickets[i][1]);
                
                dfs(tickets[i][1], tickets, visited, depth + 1);
                
                // 모든 티켓을 다 사용하기 전에 경로가 끊기는 경우 백트래킹
                visited[i] = false;
                path.remove(path.size() - 1);
            }
        }
    }
}