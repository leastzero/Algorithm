class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var last_index = num_list.lastIndex
        var num: Int = 0
        if (num_list[last_index] > num_list[last_index - 1]) {
            num = num_list[last_index] - num_list[last_index - 1]
            answer = num_list.plus(num)
        } else {
            num = num_list[last_index] * 2
            answer = num_list.plus(num)
        }
        return answer
    }
}