class Solution {
    fun solution(q: Int, r: Int, code: String): String {
        var answer: String = ""
        for (i in 0..code.length - 1) {
            if (i % q == r) answer += code[i]
        }
        return answer
    }
}