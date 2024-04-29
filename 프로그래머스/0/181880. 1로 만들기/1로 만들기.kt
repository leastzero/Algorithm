class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        for (i in num_list.indices) {
            while(true) {
                if (num_list[i] == 1) break
                if (num_list[i] % 2 == 0) {
                    num_list[i] = num_list[i] / 2
                    answer++
                }
                else {
                    num_list[i] = (num_list[i] - 1) / 2
                    answer++
                }
            }
        }
        return answer
    }
}