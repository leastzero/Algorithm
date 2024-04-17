class Solution {
    fun solution(l: Int, r: Int): IntArray {
        var answer = (l..r).filter {
            it.toString().all { s ->
                s == '0' || s == '5'
            }
        }
        if (answer.isEmpty()) {
            return intArrayOf(-1)
        } else {
            return answer.toIntArray()
        }
    }
}