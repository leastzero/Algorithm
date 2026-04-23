import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        // <아이디, 이름>
        HashMap<String, String> user = new HashMap<>();
        
        // <아이디, 메시지>
        Deque<String[]> message = new ArrayDeque<>();
        
        // 유저 맵에 아이디 없으면 아이디랑 닉네임 저장하기
        // 메시지가 엔터나 리브면 메시지 맵에 아이디랑 같이 메시지 저장하기
        // 메시지가 체인지면 유저 맵에 있는 아이디의 이름 변경
        // 메시지 맵 반복문 돌면서 메시지에 따른 출력문 출력 (아이디로 닉네임 가져오기)
        
        for (String r: record) {
            String[] order = r.split(" ");
            
            if (!user.containsKey(order[1])) {
                user.put(order[1], order[2]);
            }
            
            if (order[0].equals("Enter")) {
                if (user.containsKey(order[1])) {
                    user.put(order[1], order[2]);
                    message.offer(new String[]{order[1], order[0]});
            }
            } else if (order[0].equals("Leave")) {
                message.offer(new String[]{order[1], order[0]});
            } else {
                user.put(order[1], order[2]);
            }
        }
         
        String[] answer = new String[message.size()];
        int index = 0;
        
        while (!message.isEmpty()) {
            String[] cur = message.poll();
            String id = cur[0];
            String order = cur[1];
            
            String name = user.get(id);
            
            if (order.equals("Enter")) {
                answer[index++] = name + "님이 들어왔습니다.";
            } else {
                answer[index++] = name + "님이 나갔습니다.";
            }
        }
        
        return answer;
    }
}