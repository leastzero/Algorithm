class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = -1
        for (i in 0..num_list.size - 1) {
            if (num_list[i] < 0) {
                answer = i
                break
            }
        }
        return answer
    }
}