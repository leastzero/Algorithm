class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String cur_binary = Integer.toBinaryString(n);
        int num = 0;
        for (char cb: cur_binary.toCharArray()) {
            if (cb == '1') num += 1;
        }
        
        while (true) {
            n += 1;
            
            String next_binary = Integer.toBinaryString(n);
            int binary_num = 0;
            for (char nb: next_binary.toCharArray()) {
                if (nb == '1') binary_num += 1;
            }
            
            if (binary_num == num) {
                answer = Integer.parseInt(next_binary, 2);
                break;
            }
        }
        
        return answer;
    }
}