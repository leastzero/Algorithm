class Solution {
    fun solution(number: String): Int {
        var answer: Int = 0
        for (i in 0 until number.length) {
            answer += number[i].toInt() - '0'.toInt()
        }
        answer %= 9
        return answer
    }
}