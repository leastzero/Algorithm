class Solution {
    fun reverse(str: String): String {
        return str.reversed()
    }

    fun solution(my_string: String, queries: Array<IntArray>): String {
        var answer = my_string
        for (i in 0 until queries.size) {
            val s = queries[i][0]
            val e = queries[i][1]

            val substring = answer.substring(s, e + 1)
            val reversedSubstring = reverse(substring)
            answer = answer.substring(0, s) + reversedSubstring + answer.substring(e + 1)
        }
        return answer
    }
}