class Solution {
    fun solution(a: Int, b: Int, flag: Boolean): Int {
        var answer: Int = 0
        when (flag) {
            true -> answer = a + b
            false -> answer = a - b
        }
        return answer
    }
}