class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        int cur_time = 0;
        int cur_health = health;
        int attack_index = 0;
        int sequence = 0;
        
        while (cur_time < attacks[attacks.length - 1][0]) {
            cur_time++;
            
            if (attack_index < attacks.length && cur_time == attacks[attack_index][0]) {
                // 공격 당하는 시간이면
                sequence = 0;
                cur_health -= attacks[attack_index][1];
                attack_index++;
                
                if (cur_health <= 0) return -1;
            } else {
                // 공격 당하는 시간이 아니면
                // 체력 회복 및 연속 공격
                cur_health += bandage[1];
                sequence++;

                // 연속 공격이 시간만큼이면 추가 체력 회복
                if (sequence == bandage[0]) {
                    sequence = 0;
                    cur_health += bandage[2];
                }
                
                // 최대 체력보다 높으면 최대체력으로
                if (cur_health > health) {
                    cur_health = health;
                }
            }
        }
        
        answer = cur_health;
        
        return answer;
    }
}