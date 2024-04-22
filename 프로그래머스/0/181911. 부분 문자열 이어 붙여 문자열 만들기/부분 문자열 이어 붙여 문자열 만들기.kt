class Solution {
    fun solution(my_strings: Array<String>, parts: Array<IntArray>): String {
        var answer: String = ""
        for (i in 0..parts.size - 1) {
            var s = parts[i][0]
            var e = parts[i][1]
            answer += my_strings[i].substring(s, e + 1)
        }
        return answer
    }
}