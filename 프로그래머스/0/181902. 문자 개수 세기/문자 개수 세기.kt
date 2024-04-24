class Solution {
    fun solution(my_string: String): IntArray {
        var answer = IntArray(52)
        for (ch in my_string) {
            var index = if (ch.isUpperCase()) ch - 'A' else ch - 'a' + 26
            answer[index]++
        }
        return answer
    }
}