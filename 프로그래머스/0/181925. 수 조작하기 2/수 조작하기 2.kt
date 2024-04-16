class Solution {
    fun solution(numLog: IntArray): String {
        var answer: String = ""
        for (i in 0 until numLog.size - 1) {
            when (numLog[i] - numLog[i + 1]) {
                -1 -> answer += 'w'
                1 -> answer += 's'
                -10 -> answer += 'd'
                10 -> answer += 'a'
            }
        }
        return answer
    }
}