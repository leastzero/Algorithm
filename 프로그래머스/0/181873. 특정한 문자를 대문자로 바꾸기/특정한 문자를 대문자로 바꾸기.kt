class Solution {
    fun solution(my_string: String, alp: String): String {
        var answer: String = ""
        my_string.forEach {
            if (it.toString() == alp) answer += it.toUpperCase()
            else answer += it
        }
        return answer
    }
}