class Solution {
    fun solution(start_num: Int, end_num: Int): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in start_num until end_num + 1) {
            answer += i
        }
        return answer
    }
}