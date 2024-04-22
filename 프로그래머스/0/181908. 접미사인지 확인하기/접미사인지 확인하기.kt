class Solution {
    fun solution(my_string: String, is_suffix: String): Int {
        var answer: Int = 0
        for (i in 0..my_string.length - 1) {
            if (is_suffix == my_string.substring(i)) answer = 1
        }
        return answer
    }
}