class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        var ab = a.toString() + b.toString()
        if (ab.toInt() >= 2 * a * b) {
            answer = ab.toInt()
        } else {
            answer = 2 * a * b
        }
        return answer
    }
}