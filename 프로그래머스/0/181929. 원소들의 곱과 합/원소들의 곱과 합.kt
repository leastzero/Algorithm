class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var sum: Int = 0
        var mul: Int = 1
        for (i in 0 until num_list.size) {
            sum += num_list[i]
            mul *= num_list[i]
        }
        if (mul < sum * sum) {
            answer = 1
        }
        return answer
    }
}