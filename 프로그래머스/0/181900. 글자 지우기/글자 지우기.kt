class Solution {
    fun solution(my_string: String, indices: IntArray): String {
        var answer = my_string.filterIndexed { index, _ -> index !in indices }
        return answer
    }
}