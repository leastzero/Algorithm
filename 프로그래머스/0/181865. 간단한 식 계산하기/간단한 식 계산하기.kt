class Solution {
    fun solution(binomial: String): Int {
        var answer: Int = 0
        var list = binomial.split(" ")
        var a = list[0].toInt()
        var b = list[2].toInt()
        var op = list[1]
        answer = when(op) {
            "+" -> a + b
            "-" -> a - b
            else -> a * b
        }
        return answer
    }
}