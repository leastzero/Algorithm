class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        var ab = a.toString() + b.toString()
        var ba = b.toString() + a.toString()
        if (ab.toInt() > ba.toInt()) {
            answer = ab.toInt()
        } else {
            answer = ba.toInt()
        }
        return answer
    }
}