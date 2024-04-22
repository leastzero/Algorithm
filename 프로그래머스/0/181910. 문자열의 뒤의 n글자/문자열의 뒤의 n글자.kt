class Solution {
    fun solution(my_string: String, n: Int): String {
        var answer: String = ""
        for (i in my_string.length - 1 downTo 0) {
            if (answer.length == n) break
            answer += my_string[i]
        }
        return answer.reversed()
    }
}