class Solution {
    fun solution(ineq: String, eq: String, n: Int, m: Int): Int {
        var answer: Int = 0
        var a = ineq + eq
        when (a) {
            ">=" -> if (n >= m) answer = 1
            "<=" -> if (n <= m) answer = 1
            ">!" -> if (n > m) answer = 1
            "<!" -> if (n < m) answer = 1
        }
        return answer
    }
}