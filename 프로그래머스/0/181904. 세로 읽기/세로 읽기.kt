class Solution {
    fun solution(my_string: String, m: Int, c: Int): String {
        var answer: String = ""
        for (i in 0..my_string.length step m) {
            if (i + m > my_string.length) break
            var cut_string = my_string.substring(i, i + m)
            answer += cut_string[c - 1]
        }
        return answer
    }
}